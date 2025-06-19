import json
from jsoncontroller import JsonController as JC

class Deck():
    def __init__(self, title=None):
        self.title = title
        self.JsonController = JC('data/deck.json')

    def load_deck_data(self):
        try:
             data = self.JsonController.open_file()
             print(data)
        except (json.JSONDecodeError, FileNotFoundError):
            print('El archivo esta vacio o no existe, crea una tarjeta primero') 

    def add_deck(self):
                try:
                    data = self.JsonController.open_file()  
                    
                    if self.title in data:
                         print('El nombre de el deck ya existe, pruebe con otro')
                    else:    
                        data[self.title] = {}
                        self.JsonController.save_file(data)
                        print(data)

                except (json.JSONDecodeError, FileNotFoundError):
                    data[self.title] = {}
                    self.JsonController.save_file(data)
                    print(data)

    def remove_deck(self):
        data = self.JsonController.open_file()
        if self.title in data:
             del data[self.title]
             self.JsonController.save_file(data)
        
        else:
             print('El mazo no existe.')
        