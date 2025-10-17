from reports.average_rating import avarage_rating
from reports.csv_utils import read_csv_files


def test_average_rating_simple_case():
    data = [
        {"name": "iphone 15 pro",
         "brand": "apple",
         "price": "999",
         "rating": "4.9"
         },

        {
            "name": "galaxy s23 ultra",
            "brand": "samsung",
            "price": "1199",
            "rating": "4.8",
        },

        {"name": "redmi note 12",
         "brand": "xiaomi",
         "price": "199",
         "rating": "4.6"
         },

        {"name": "iphone 14",
         "brand": "apple",
         "price": "799",
         "rating": "4.7"
         },

        {"name": "galaxy a54",
         "brand": "samsung",
         "price": "349",
         "rating": "4.2"
         },

        {"name": "poco x5 pro",
         "brand": "xiaomi",
         "price": "299",
         "rating": "4.4"
         },

        {"name": "iphone se",
         "brand": "apple",
         "price": "429",
         "rating": "4.1"
         },

        {
            "name": "galaxy z flip 5",
            "brand": "samsung",
            "price": "999",
            "rating": "4.6",
        },

        {"name": "redmi 10c",
         "brand": "xiaomi",
         "price": "149",
         "rating": "4.1"
         },

        {"name": "iphone 13 mini",
         "brand": "apple",
         "price": "599",
         "rating": "4.5"
         },
    ]

    test_data = [
        {"id": 1, "brand": "apple", "raiting": 4.55},
        {"id": 2, "brand": "samsung", "raiting": 4.53},
        {"id": 3, "brand": "xiaomi", "raiting": 4.37},
    ]

    result = avarage_rating(data)

    assert test_data == result


def test_read_csv_files(tmp_path):
    test_file = tmp_path / "test.csv"
    test_file.write_text(
        "name,brand,price,rating\n"
        "iphone 15 pro,apple,999,4.9\n"
        "galaxy s23 ultra,samsung,1199,4.8\n"
    )

    result = read_csv_files([str(test_file)])

    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["brand"] == "apple"
    assert result[1]["rating"] == "4.8"
