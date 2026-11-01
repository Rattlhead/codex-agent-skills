#!/usr/bin/env python3
"""Validate one request/reply. Does not grant permission or execute any action."""
import argparse
import json
from pathlib import Path
from decision_contract import input_errors, output_errors, strict_loads


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--request',required=True,help='Single request JSON object, not JSONL.')
    parser.add_argument('--response',required=True,help='Single reply JSON object, not JSONL.')
    args=parser.parse_args()
    try:
        request=strict_loads(Path(args.request).read_text())
        response=strict_loads(Path(args.response).read_text())
        errors=input_errors(request)
        if not errors: errors=output_errors(response,request)
    except (OSError,ValueError,TypeError) as error:
        errors=[str(error)]
    print(json.dumps({'valid':not errors,'errors':errors,'scope':'Structure, status invariants and IDs/options only. Semantic authority, evidence truth, execution and user approval remain controller responsibilities.'},indent=2))
    return 1 if errors else 0

if __name__=='__main__':
    raise SystemExit(main())
