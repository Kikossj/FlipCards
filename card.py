import json
import jsoncontroller

class Card():
    def __init__(self, title, desc):
        self.title = title
        self.desc = desc
        self.JsonController = []

    def add_card(self):
        try:
            ctrl = jsoncontroller.JsonController('data/cards.json')
            data = ctrl.open_file()
            self.title = input('Titulo de la tarjeta: ')

            if self.title in data:
                print('La tarjeta ya existe')
            else:
                self.desc = input('Descripcion de la tarjeta: ')
                data[self.title] = self.desc
                ctrl.save_file(data)
                print(data)

        except json.JSONDecodeError:
            self.title = input('Titulo de la tarjeta: ')
            self.desc = input('Descripcion de la tarjeta: ')
            data[self.title] = self.desc
            ctrl.save_file(data)
            print(data)

    def load_card(self):
        try:
            data = jsoncontroller.JsonController('data/cards.json')
            print(data)
            
        except json.JSONDecodeError:
            print('El archivo esta vacio o no existe, crea una tarjeta primero')