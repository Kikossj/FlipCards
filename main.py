import json, card, deck
from colorama import Fore

class Menu():
    def run(self):
        while True:
            print('¿Que quieres hacer?')
            print(
                '1. Crear tarjeta' '\n2. Ver tarjetas'
                '\n3. Crear mazo' '\n4. Ver mazos'
            )
            opt = input('Opción: ')
            if opt == 1:
                card.Card.add_card()
            elif opt == 2:
                card.Card.load_card()
            elif opt == 3:
                deck.Deck.add_deck()
            elif opt == 4:
                deck.Deck.load_deck_data()



ru = Menu()
ru.run()