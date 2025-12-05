from service.PenguinService import PenguinService
from domain.PenguinValidator import PenguinValidator
from repository.PenguinFileRepo import PenguinFileRepo
from ui.console import Console
from utils.utils import *

def main():
    #app_preload()
    # #creating our second dataset

    try:
        while True:
            command=str(input())
            #possible commands
            if command == "help":
                Console.print_menu()
            elif command == "quit":
                break
            elif command == "print available data":
                Console.print_available_data()
            elif "load" in command:
                Console.load_file()
            elif "filter" in command:
                Console.filter_data()
            elif "describe" in command:
                Console.describe_attribute()
            elif "unique" in command:
                Console.unique_attribute()
            elif "sort" in command:
                Console.sort_by_attribute()
            elif "augment" in command:
                Console.augment_dataset()
            elif "scatter" in command:
                Console.create_scatter()
            elif "hist" in command:
                Console.create_histogram()
            elif "boxplot" in command:
                Console.create_boxplot()
            else:
                print("Unkonwn command. Use help to see all available commands")
    except KeyboardInterrupt: #cant quit like this
        return

main()
