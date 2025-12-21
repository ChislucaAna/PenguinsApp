from domain.Penguin import Penguin
from repository.PenguinRepo import PenguinFileRepo
class PenguinService:
    def __init__(self,repo:PenguinFileRepo,fields):
        self.__repo=repo
        self.__fields=fields

    def save_to_file(self, penguins, fields):
        self.__repo.write_to_file(penguins,fields)

    def load_from_file(self, fields):
        return self.__repo.read_from_file(fields)
    
    def create_new_dataset(self, filename, fields, accept_null_values):
        penguins = self.load_from_file(fields)
        if not accept_null_values:
            penguins = [
                p for p in penguins
                if all(getattr(p, field, None) not in (None, "") for field in fields)
            ]
        new_repository = PenguinFileRepo(filename)
        new_service = PenguinService(new_repository, fields)
        new_service.save_to_file(penguins, fields)