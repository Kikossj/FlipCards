import json, card, deck
from colorama import Fore

class Menu():
    def run(self):
        cards = card.Card('','')
        decks = deck.Deck()

        while True:
            print('¿Que quieres hacer?')
            print(
                '1. Crear tarjeta' '\n2. Ver tarjetas'
                '\n3. Crear mazo' '\n4. Ver mazos'
                '\n5. Salir'
            )
            opt = int(input('Opción: '))
            if opt == 1:
                cards.add_card()
            elif opt == 2:
                cards.load_card()
            elif opt == 3:
                decks.add_deck()
            elif opt == 4:
                decks.load_deck_data()
            elif opt == 5:
                break



ru = Menu()
ru.run()