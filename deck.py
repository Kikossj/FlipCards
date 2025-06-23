import json
from jsoncontroller import JsonController as JC
from card import Card
import random

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
        try:
            data = self.JsonController.open_file()

            if self.title in data:
                del data[self.title]
                self.JsonController.save_file(data)
            
            else:
                print('El mazo no existe.')

        except (json.JSONDecodeError, FileNotFoundError):
             print('Ha ocurrido un error encontrando el archivo')

    def cardto_deck(self, card_title):
        self.card_title = card_title
        card = Card(card_title)
        cards = JC('data/cards.json').open_file()
        data = self.JsonController.open_file()

        if card_title in cards and self.title in data:
            data[self.title][card_title] = cards[card_title]
            self.JsonController.save_file(data)

        elif card not in cards:
            print('La tarjeta no existe')

        elif self.title not in data:
            print('El mazo no existe')
    
    def del_cardof_deck(self, card_title):
        self.card_title = card_title
        data = self.JsonController.open_file()
        if card_title in self.title:
            del data[self.title][card_title]
            self.JsonController.save_file(data)

    def get_randomcard(self):
        data = self.JsonController.open_file()
        
        if self.title in data:
             sel_deck = data[self.title]
             key = random.choice(list(sel_deck.keys()))
             value = sel_deck[key]             
             return key, value
        else:
             print('Seleccione un mazo valido')

    def quiz_user(self, rounds=None):
        title = input('Ingrese titulo: ').title()
        decks = Deck(title)
        self.rounds = rounds
        points = 0
        for _ in range(rounds):
            key, value = decks.get_randomcard()
            print(key)
            answ = input('Respuesta: ')
            if answ.title() == value.title():
                points += 1
                print(f'¡Correcto, tienes {points} puntos!')
            else:
                print('No es correcto')
        print(f'Puntuacion final de {points} puntos.')
