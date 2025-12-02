import argparse
import sys

from pathlib import Path
from typing import List

from reports.reader import read_csv_files
from reports.report import Report, PerformanceReport

REPORTS: dict[str, Report] = {
    'performance': PerformanceReport(),
}

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Employee reports generator")
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        type=Path,
    )
    parser.add_argument(
        "--report",
        required=True,
        choices=list(REPORTS.keys()),
    )
    return parser

def main(argv: List[str] | None = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)

    missing = [p for p in args.files if not p.exists()]
    if missing:
        print(f"Error: Files not found: {' '.join(str(p) for p in missing)}",
              file=sys.stderr)
        sys.exit(1)
    data = read_csv_files(args.files)
    report = REPORTS[args.report]
    print(report.generate(data))

if __name__ == "__main__":
    main()

