import json
from jsoncontroller import JsonController as JC

class Card():
    def __init__(self, title=None, desc=None):
        self.title = title
        self.desc = desc
        self.JsonController = JC('data/cards.json')

    def add_card(self):
        try:
            data = self.JsonController.open_file()

            if self.title in data:
                print('La tarjeta ya existe')
            else:
                data[self.title] = self.desc
                self.JsonController.save_file(data)
                print(data)

        except (json.JSONDecodeError, FileNotFoundError):
            data[self.title] = self.desc
            self.JsonController.save_file(data)
            print(data)

    def load_card(self):
        try:
            data = self.JsonController.open_file()
            print(data)

        except (json.JSONDecodeError, FileNotFoundError):
            print('El archivo esta vacio o no existe, crea una tarjeta primero')
    
    def remove_card(self):
        data = self.JsonController.open_file()
        if self.title in data:
             del data[self.title]
             self.JsonController.save_file(data)
        
        else:
             print('La tarjeta no existe no existe.')
        