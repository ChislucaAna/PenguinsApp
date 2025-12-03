from repository.PenguinFileRepo import PenguinFileRepo
from domain.PenguinValidator import PenguinValidator
from domain.Penguin import Penguin

class PenguinService:
    """
    Service layer for managing Penguin-related operations.
    """
    def __init__(self, penguin_repo:PenguinFileRepo, penguin_validator:PenguinValidator,special_validation=False):
        self.__special_validation = special_validation #required for task1
        self.__penguin_repo=penguin_repo
        self.__penguin_validator=penguin_validator

    def add_penguin(self,penguin:Penguin):
        """
        :param penguin: Penguins to add
        adds a penguin taking into the account possible non_empty field
        validations required for task1
        """
        if self.__special_validation:
            try:
                self.__penguin_validator.validate_special_fields(penguin)
                self.__penguin_repo.add_penguin(penguin)
            except ValueError:
                return
        else:
            self.__penguin_repo.add_penguin(penguin)

    def get_all_penguins(self):
        return self.__penguin_repo.get_all_penguins()