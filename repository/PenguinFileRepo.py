from pygments.lexer import using
from datetime import *
from domain.Penguin import Penguin
import csv
import os


class PenguinFileRepo:
    def __init__(self, filename):
        self.__filename = os.path.abspath(filename)

    def __load_form_file(self):
        """
        Load the penguins from file
        :return: a list of penguins build based on the file content
        """

        # handles the case in which the file does not exist
        if not os.path.exists(self.__filename):
            with open(self.__filename, "w"):  # creates empty file
                pass
            return []

        penguins = []
        with open(self.__filename, "r") as file:
            lines = csv.reader(file)  # list with all lines
            for line in lines:
                # Skip empty lines or lines with all empty fields
                if not line or all(field.strip() == '' for field in line):
                    print(f"Skipping empty line: {line}")
                    continue

                try:
                    (study_name, sample_number, species, region, island, stage, individual, clutch_completion,
                     date_egg, culmen_length, culmen_depth, flipper_length, body_mass, sex, delta_15_n, delta_13_c,
                     comments) = line
                except ValueError as e:
                    print(f"Wrong number of fields in line. Expected 17, got {len(line)}: {line}")
                try:
                    # Try to parse date in multiple formats
                    date_parsed = None
                    for date_format in ["%Y-%m-%d","%m/%d/%Y"]:
                        try:
                            date_parsed = datetime.strptime(date_egg, date_format).date()
                            break
                        except ValueError:
                            continue

                    if date_parsed is None:
                        raise ValueError(f"Could not parse date '{date_egg}' with any known format")

                    penguin = Penguin(study_name, int(sample_number), species, region, island, stage, individual,
                                      clutch_completion,
                                      date_parsed, float(culmen_length), float(culmen_depth),
                                      int(flipper_length), int(body_mass), sex, float(delta_15_n), float(delta_13_c),
                                      comments)
                except ValueError as e:
                    print(f"Invalid data in line: {line}, {e}")
                    continue
                penguins.append(penguin)

        return penguins

    def __save_to_file(self, penguins: list[Penguin]):
        """
        Write a penguins list to file
        """
        open(self.__filename, "w", newline="").close()
        with open(self.__filename, "a", newline="") as file:
            writer = csv.writer(file)
            for p in penguins:
                writer.writerow(p.to_csv_row())

    def add_penguin(self, penguin: Penguin):
        penguins = self.__load_form_file()
        penguins.append(penguin)
        self.__save_to_file(penguins)

    def get_all_penguins(self):
        return self.__load_form_file()