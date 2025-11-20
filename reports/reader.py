import csv
from pathlib import Path
from typing import List

from report.types import EmployeeDict


def read_csv_files(paths:List[Path]) -> List[EmployeeDict]:
    all_rows: List[EmployeeDict] = []
    for path in paths:
        with path.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                cleaned = {k.strip(): v.strip() for k, v in row.items()}
                all_rows.append(cleaned)
    return all_rows