from collections import defaultdict
from statistics import mean


def avarage_rating(data):
    brand_dict = defaultdict(list)
    for key in data:
        brand_dict[key["brand"]].append(float(key["rating"]))

    report = []
    id = 1
    for brand, rating in brand_dict.items():
        v = dict(id=id, brand=brand, raiting=round(mean(rating), 2))
        report.append(v)
        id += 1
    report.sort(key=lambda x: ["rating"], reverse=True)
    return report
