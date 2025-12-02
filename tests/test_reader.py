import csv
from pathlib import Path

from reports.reader import read_csv_files


def test_read_csv_files_combines_multiple_files(tmp_path: Path):
    file1 = tmp_path / "f1.csv"
    file2 = tmp_path / "f2.csv"

    with file1.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["position", "performance"])
        writer.writeheader()
        writer.writerow({"position": "Backend", "performance": "4.8"})

    with file2.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["position", "performance"])
        writer.writeheader()
        writer.writerow({"position": "DevOps", "performance": "5.0"})

    data = read_csv_files([file1, file2])

    assert len(data) == 2
    positions = {row["position"] for row in data}
    assert positions == {"Backend", "DevOps"}