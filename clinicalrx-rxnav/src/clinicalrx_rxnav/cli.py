import argparse, json, logging, sys
from .client import RxNavClient, RxNavError

def main():
    parser = argparse.ArgumentParser(prog="rxnav", description="Query official NLM RxNav APIs")
    sub = parser.add_subparsers(dest="command", required=True)
    p=sub.add_parser("name"); p.add_argument("term")
    p=sub.add_parser("drug"); p.add_argument("rxcui")
    p=sub.add_parser("related"); p.add_argument("rxcui"); p.add_argument("--tty")
    p=sub.add_parser("class"); p.add_argument("rxcui")
    p=sub.add_parser("rxterms"); p.add_argument("rxcui")
    p=sub.add_parser("rxmix"); p.add_argument("operations")
    parser.add_argument("--verbose", action="store_true")
    args=parser.parse_args(); logging.basicConfig(level=logging.INFO if args.verbose else logging.WARNING)
    api=RxNavClient()
    try:
        if args.command=="name": result=api.find_rxcui(args.term)
        elif args.command=="drug": result=api.get_drug(args.rxcui)
        elif args.command=="related": result=api.get_related(args.rxcui,args.tty)
        elif args.command=="class": result=api.get_class_by_rxcui(args.rxcui)
        elif args.command=="rxterms": result=api.get_rxterms_by_rxcui(args.rxcui)
        else: result=api.run_rxmix(args.operations)
        print(json.dumps(result, indent=2, ensure_ascii=False))
    except (RxNavError, ValueError) as exc:
        logging.error("%s", exc); sys.exit(2)

if __name__ == "__main__": main()
