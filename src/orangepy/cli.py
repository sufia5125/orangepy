import argparse
import json
import numpy as np
from orangepy import inspect
import sys

def main()->int:
    parser = argparse.ArgumentParser(
        prog="orangepy",
    )
    parser.add_argument("file", help="path to a .npy file")
    parser.add_argument("--json", help="print the report in JSON")
    
    args = parser.parse_args()
    
    try:
        data = np.load(args.file, allow_pickle=False)
        report = inspect(data)
    except(OSError, ValueError, TypeError) as e:
        print(f"orangepy: error {e}", file=sys.stderr)
        return 2
    
    if args.json:
        payload = report.to_dict()
        payload["issues"]= report.issues
        print(json.dumps(payload, indent=2))
    else:
        print(report.summary())
    
    return 1 if report.issues else 0

if __name__ == "__main__":
    raise SystemExit(main())