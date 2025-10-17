import argparse
from tabulate import tabulate
from reports.average_rating import avarage_rating
from reports.csv_utils import read_csv_files

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--files", nargs="+", required=True)
    parser.add_argument("--report", required=True)
    args = parser.parse_args()

    data = read_csv_files(args.files)

    report = avarage_rating(data)

    print(tabulate(report, headers="keys", tablefmt="grid"))
