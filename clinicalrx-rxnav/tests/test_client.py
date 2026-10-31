import pytest, responses
from clinicalrx_rxnav import RxNavClient, RxNavError

@responses.activate
def test_find_rxcui():
    responses.add(responses.GET, "https://rxnav.nlm.nih.gov/REST/rxcui.json", json={"idGroup":{"rxnormId":["5640"]}}, status=200)
    assert RxNavClient(max_retries=0, cache_ttl_seconds=0).find_rxcui("ibuprofen")["idGroup"]["rxnormId"] == ["5640"]

def test_empty_name():
    with pytest.raises(ValueError): RxNavClient().find_rxcui(" ")

@responses.activate
def test_retry_503():
    url="https://rxnav.nlm.nih.gov/REST/drugs/5640.json"
    responses.add(responses.GET,url,status=503); responses.add(responses.GET,url,json={"drugGroup":{}},status=200)
    assert RxNavClient(max_retries=1,backoff_seconds=0,cache_ttl_seconds=0).get_drug("5640")=={"drugGroup":{}}

@responses.activate
def test_reject_non_json():
    responses.add(responses.GET,"https://rxnav.nlm.nih.gov/REST/drugs/5640.json",body="not json",status=200)
    with pytest.raises(RxNavError): RxNavClient(max_retries=0,cache_ttl_seconds=0).get_drug("5640")
