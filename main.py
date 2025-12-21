from ui.Console import Console
from service.PenguinService import PenguinService
from repository.PenguinRepo import PenguinFileRepo
from domain.Penguin import Penguin
from utils import DEFAULT_FIELDS

repo = PenguinFileRepo("penguins.csv")
service = PenguinService(repo,DEFAULT_FIELDS)
penguins=service.load_from_file(DEFAULT_FIELDS)
console = Console(service)

console.run()
