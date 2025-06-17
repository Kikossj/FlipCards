import json
from colorama import Fore

#---Contenedor de tarjetas---
class Deck():
    def __init__(self):
        pass

    def load_deck_data(self):
        with open(r'C:\Users\denja\OneDrive\Desktop\ConquerBlocks\Python\FlipCards\deck.json', 'r+', encoding="utf-8") as file:
            deck_data = json.load(file)
        print(deck_data)
        return deck_data
        

    def add_deck(self):
        
        while True:
            opt = input('¿Quieres crear un deck? S/N')
            if opt.lower() == 's':
                try:
                    decks_data = Deck.load_deck_data(self)  
                    deck_name = input("Elige un nombre para el mazo: ")
                        
                    if deck_name in decks_data:
                         print('El nombre de el deck ya existe, pruebe con otro')
                    else:    
                        decks_data[deck_name] = {}
    
                        with open (r'C:\Users\denja\OneDrive\Desktop\ConquerBlocks\Python\FlipCards\deck.json', 'w+') as file:
                            json.dump(decks_data, file, indent=4, ensure_ascii=False)

                except json.decoder.JSONDecodeError:
                    deck_name = input("Elige un nombre para el mazo: ")
                    decks_data[deck_name] = {}
    
                    with open (r'C:\Users\denja\OneDrive\Desktop\ConquerBlocks\Python\FlipCards\deck.json', 'w+') as file:
                        json.dump(decks_data, file, indent=4, ensure_ascii=False)
            else:
                break

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

        with open(r'C:\Users\denja\OneDrive\Desktop\ConquerBlocks\Python\FlipCards\cards.json', 'a') as file:
            tarjetas = json.dump(tarjetas, file, indent=4, ensure_ascii=False)
        print(f'tarjeta con nombre: {title} con descripcion: {desc}.')



tarjeta = Card()
deck = Deck()
deck.add_deck()
deck.load_deck_data()