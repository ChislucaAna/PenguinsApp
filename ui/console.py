from service.PenguinService import PenguinService
from pathlib import Path

class Console:
    """Console-based UI for interacting with penguin service."""

    def __init__(self, penguin_service:PenguinService):
        self.__penguin_service = penguin_service

    @staticmethod
    def print_menu():
        print("Available commands:")
        print(">print available_data")
        print(">load <filename>")
        print(">filter <attribute> <value>")
        print(">describe <attribute>")
        print(">unique <attribute>")
        print(">sort <attribute> <asc|desc>")
        print(">augument <precent> <duplicate|create>")
        print(">scatter <attribute1> <attribute2>")
        print(">hist <attribute> <bins>")
        print(">boxplot <island | species> attribute")
        print(">help")
        print(">quit")

    @staticmethod
    def print_available_data():
        datasets_dir = Path("datasets")  # relative to your project root

        for csv_file in datasets_dir.glob("*.csv"):
            print(csv_file)

    def load_file(self):
        pass

    def filter_data(self):
        pass

    def describe_attribute(self):
        pass

    def unique_attribute(self):
        pass

    def sort_by_attribute(self):
        pass

    def augment_dataset(self):
        pass

    def create_scatter(self):
        pass

    def create_histogram(self):
        pass

    def create_boxplot(self):
        pass