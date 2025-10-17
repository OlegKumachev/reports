import csv


def read_csv_files(file_list):
    data = []
    for file in file_list:
        with open(file, "r", newline="", encoding="utf-8") as csvfile:

            s = csv.DictReader(csvfile)
            for row in s:
                data.append(row)
    return data
