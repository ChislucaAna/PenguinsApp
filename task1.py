from domain.PenguinValidator import PenguinValidator
from repository.PenguinFileRepo import PenguinFileRepo
from service.PenguinService import PenguinService

validator = PenguinValidator()
base_repo = PenguinFileRepo("datasets/penguins.csv")
base_service= PenguinService(base_repo,validator,False)
base_list = base_service.get_all_penguins()
special_repo = PenguinFileRepo("datasets/penguins_data.csv")
special_service = PenguinService(special_repo,validator,True)
for penguin in base_list:
    special_service.add_penguin(penguin)
    print("Adding")