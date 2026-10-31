from __future__ import annotations
import logging, os, time
from typing import Any, Dict, Optional, Tuple
from urllib.parse import quote
import requests

logger = logging.getLogger("clinicalrx_rxnav")

class RxNavError(RuntimeError):
    pass

class RxNavHTTPError(RxNavError):
    def __init__(self, status_code: int, message: str):
        super().__init__(message)
        self.status_code = status_code

class RxNavClient:
    BASE_URL = "https://rxnav.nlm.nih.gov/REST"

    def __init__(self, timeout: Tuple[float, float] = (3.05, 15.0), max_retries: int = 3,
                 backoff_seconds: float = 0.5, cache_ttl_seconds: int = 300,
                 session: Optional[requests.Session] = None, api_key: Optional[str] = None):
        self.timeout = timeout
        self.max_retries = max(0, max_retries)
        self.backoff_seconds = max(0.0, backoff_seconds)
        self.cache_ttl_seconds = max(0, cache_ttl_seconds)
        self.session = session or requests.Session()
        self.api_key = api_key or os.getenv("RXNAV_UTS_API_KEY")
        self._cache: Dict[str, tuple[float, Dict[str, Any]]] = {}
        self.session.headers.update({"Accept": "application/json", "User-Agent": "ClinicalRx-RxNav/0.1.0"})
        if self.api_key:
            self.session.headers["Authorization"] = f"Bearer {self.api_key}"

    def _get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        path = endpoint.lstrip("/")
        url = f"{self.BASE_URL}/{path}"
        cache_key = requests.Request("GET", url, params=params).prepare().url or url
        cached = self._cache.get(cache_key)
        if cached and cached[0] > time.monotonic():
            return cached[1]
        last_error = None
        for attempt in range(self.max_retries + 1):
            try:
                response = self.session.get(url, params=params, timeout=self.timeout)
                if (response.status_code == 429 or 500 <= response.status_code < 600) and attempt < self.max_retries:
                    retry_after = response.headers.get("Retry-After", "")
                    delay = float(retry_after) if retry_after.isdigit() else self.backoff_seconds * (2 ** attempt)
                    time.sleep(min(delay, 20.0))
                    continue
                try:
                    response.raise_for_status()
                except requests.HTTPError as exc:
                    status = response.status_code
                    raise RxNavHTTPError(status, f"RxNav HTTP request failed ({status})") from exc
                try:
                    payload = response.json()
                except ValueError as exc:
                    raise RxNavError("RxNav returned non-JSON content") from exc
                if not isinstance(payload, dict):
                    raise RxNavError("RxNav response was not a JSON object")
                if self.cache_ttl_seconds:
                    self._cache[cache_key] = (time.monotonic() + self.cache_ttl_seconds, payload)
                return payload
            except (requests.Timeout, requests.ConnectionError) as exc:
                last_error = exc
                if attempt < self.max_retries:
                    time.sleep(min(self.backoff_seconds * (2 ** attempt), 20.0))
                    continue
            except RxNavError:
                raise
            except requests.RequestException as exc:
                last_error = exc
                if attempt < self.max_retries:
                    time.sleep(min(self.backoff_seconds * (2 ** attempt), 20.0))
                    continue
        logger.warning("RxNav request failed after retries: endpoint=%s", path)
        raise RxNavError(f"RxNav request failed after {self.max_retries + 1} attempts") from last_error

    def find_rxcui(self, name: str, search: str = "0") -> Dict[str, Any]:
        if not name or not name.strip(): raise ValueError("name must not be empty")
        return self._get("rxcui.json", {"name": name.strip(), "search": search})

    def get_drug(self, rxcui: str) -> Dict[str, Any]:
        return self._get(f"drugs/{quote(str(rxcui), safe='')}.json")

    def get_related(self, rxcui: str, tty: Optional[str] = None) -> Dict[str, Any]:
        return self._get(f"rxcui/{quote(str(rxcui), safe='')}/related.json", {"tty": tty} if tty else None)

    def get_all_concepts(self, tty: Optional[str] = None) -> Dict[str, Any]:
        return self._get("allconcepts.json", {"tty": tty} if tty else None)

    def get_spelling_suggestions(self, name: str) -> Dict[str, Any]:
        if not name or not name.strip(): raise ValueError("name must not be empty")
        return self._get("spellingsuggestions.json", {"name": name.strip()})

    def get_class_by_rxcui(self, rxcui: str, rela: Optional[str] = None) -> Dict[str, Any]:
        params = {"rxcui": str(rxcui)}
        if rela: params["rela"] = rela
        return self._get("rxclass/class/byRxcui.json", params)

    def get_drugs_by_class(self, class_id: str, class_type: str) -> Dict[str, Any]:
        if not class_id or not class_type: raise ValueError("class_id and class_type are required")
        return self._get("rxclass/drugs.json", {"classId": class_id, "classType": class_type})

    def get_rxterms_by_rxcui(self, rxcui: str) -> Dict[str, Any]:
        return self._get(f"RxTerms/rxcui/{quote(str(rxcui), safe='')}.json")

    def get_rxterms_all(self) -> Dict[str, Any]:
        return self._get("RxTerms/all.json")

    def run_rxmix(self, operations: str) -> Dict[str, Any]:
        if not operations or not operations.strip(): raise ValueError("operations must not be empty")
        return self._get("RxMix", {"operations": operations})
