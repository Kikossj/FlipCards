import json
from colorama import Fore

#---Contenedor de tarjetas---
class Deck():
    def __init__(self):
        pass

    def load_deck_data(self):
        with open('data\deck.json', 'r+', encoding="utf-8") as file:
            deck_data = json.load(file)
        print(deck_data)
        return deck_data
        

    def add_deck(self):
        
        while True:
            opt = input('¿Quieres crear un deck? S/N').lower()
            if opt == 's':
                try:
                    decks_data = Deck.load_deck_data(self)  
                    deck_name = input("Elige un nombre para el mazo: ")
                        
                    if deck_name in decks_data:
                         print('El nombre de el deck ya existe, pruebe con otro')
                    else:    
                        decks_data[deck_name] = {}
    
                        with open ('data\deck.json', 'w+') as file:
                            json.dump(decks_data, file, indent=4, ensure_ascii=False)

                except json.decoder.JSONDecodeError:
                    deck_name = input("Elige un nombre para el mazo: ")
                    decks_data[deck_name] = {}
    
                    with open ('data\deck.json', 'w+') as file:
                        json.dump(decks_data, file, indent=4, ensure_ascii=False)
            else:
                break

    def remove_deck(self):

        while True:
            opt = input('¿Quieres borrar un deck? S/N').lower()
            if opt == 's':
                try:
                    decks_data = Deck.load_deck_data()
                    deck_name = input('¿Cual deseas eliminar?')

                    if deck_name in decks_data:
                        del decks_data[deck_name]
                        print()
                    else:
                        print('El deck no existe')
                except json.decoder.JSONDecodeError:
                    pass
    
#---Tarjetas---
class Card():
    def __init__(self):
        pass
    
    def add_card(self):
        title = input("Titulo de la tarjeta: ")
        desc = input("Descripcion de la tarjeta: ")
        
        tarjetas = {
            "titulo": "descripcion",
            "titulo2": "descripcion2"
        }

        tarjetas[title] = desc

        with open('data\cards.json', 'a') as file:
            tarjetas = json.dump(tarjetas, file, indent=4, ensure_ascii=False)
        print(f'tarjeta con nombre: {title} con descripcion: {desc}.')



tarjeta = Card()
deck = Deck()
deck.add_deck()
deck.load_deck_data()