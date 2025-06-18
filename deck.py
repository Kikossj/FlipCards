import json
import jsoncontroller

class Deck():
    def __init__(self):
        pass

    def load_deck_data(self):
        try:
             data = jsoncontroller.JsonController('data/deck.json')
             print(data)
        except json.JSONDecodeError:
            print('El archivo esta vacio o no existe, crea una tarjeta primero') 

    def add_deck(self):
                try:
                    ctrl = jsoncontroller.JsonController('data/deck.json')  
                    data = ctrl.open_file()
                    deck_name = input("Elige un nombre para el mazo: ")
                        
                    if deck_name in data:
                         print('El nombre de el deck ya existe, pruebe con otro')
                    else:    
                        data[deck_name] = {}
                        ctrl.save_file(data)
                        print(data)

                except json.decoder.JSONDecodeError:
                    deck_name = input("Elige un nombre para el mazo: ")
                    data[deck_name] = {}
                    ctrl.save_file(data)
                    print(data)

    def remove_deck(self):
        pass