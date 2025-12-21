import csv
from domain.Penguin import Penguin
from utils import CSV_TO_PENGUIN_FIELD_MAP
class PenguinFileRepo:
    def __init__(self,filename):
        self.__filename="datasets/"+filename

    def write_to_file(self, penguins, fields):
        
        rows = [
            {field: getattr(p, field) for field in fields}
            for p in penguins
        ]
        self._write_csv(rows)


    def _write_csv(self, rows):
        if not rows:
            return

        fieldnames = list(rows[0].keys())

        with open(self.__filename, mode="w", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
    
    def read_from_file(self, fields):
        penguins = []

        with open(self.__filename, mode="r", newline="", encoding="utf-8-sig") as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                filtered = {}

                for csv_col, penguin_attr in CSV_TO_PENGUIN_FIELD_MAP.items():
                    if penguin_attr in fields:
                        # use .get() to avoid KeyError
                        value = row.get(csv_col)
                        filtered[penguin_attr] = value

                penguins.append(Penguin.from_dict(filtered))

        return penguins
