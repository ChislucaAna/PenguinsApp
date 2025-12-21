from service.PenguinService import PenguinService
from utils import str_to_bool
class Console:
    def __init__(self,service:PenguinService):
        self.__service=service

    def print_menu(self):
        print("new_dataset [filename] [accept_null_values] [fields]-creates a new dataset with only the specified fields")

    def run(self):
        self.__service.create_new_dataset("penguins_data.csv",[
            "species",
            "flipper_length_mm",
            "culmen_length_mm",
            "culmen_depth_mm",
            "body_mass_g",
            "island",
            "sex"
        ],False)
        self.print_menu()
        while(True):
            user_input=input()
            parts=user_input.split(" ")
            cmd=parts[0]
            parameters=parts[1:]
            if(cmd=="new_dataset"):
                self.__service.create_new_dataset(parameters[0],parameters[2:],str_to_bool(parameters[1]))
                print("dataset created succesfully")
            