import json
from card import Card
from deck import Deck
from colorama import Fore

class Menu():
    def run(self):
        while True:
            print('---Menu---'
                    '\n1. Tarjetas' '\n2. Mazos'
                    '\n3. Opciones' '\n4 Salir')
            opt = int(input('Opción: '))

            if opt == 1:
                print('---Tarjetas---'
                        '\n1. Lista de tarjetas' '\n2. Crear tarjeta'
                        '\n3, Eliminar tarjeta' '\n4. Atras')
                opt = int(input('Opción: '))

                if opt == 1:
                    cards = Card()
                    cards.load_card()

                elif opt == 2:
                    title = input('Ingrese titulo: ')
                    desc = input('Ingrese descripcion: ')
                    cards = Card(title, desc)
                    cards.add_card()

                elif opt == 3:
                    title = input('Ingrese titulo: ')
                    cards = Card(title,)
                    cards.remove_card()
                    cards.add_card()
                
                elif opt == 4:
                    continue
                else:
                    print('Escoja una opcion valida.')

            elif opt == 2:
                print('---Mazos---'
                    '\n1. Lista de mazos' '\n2. Crear mazo'
                    '\n3, Eliminar mazo' '\n4. Atras')
                opt = int(input('Opción: '))

                if opt == 1:
                    decks = Deck()
                    decks.load_deck_data()

                elif opt == 2:
                    title = input('Ingrese titulo: ')
                    decks = Deck(title)
                    decks.add_deck()

                elif opt == 3:
                    title = input('Ingrese titulo: ')
                    decks = Deck(title)
                    decks.remove_deck()
                
                elif opt == 4:
                    continue
                else:
                    print('Escoja una opcion valida.')
        
            elif opt == 3:
                print('---Ajustes---'
                    '\n1. Cambiar color' '\n2. Atras')
                opt = int(input('Opción: '))

                if opt == 1:
                    print('Colores: ')
                    print(
                            '1. Color azul' '\n2. Color rojo'
                            '\n3. Color magenta' '\n4. Color verde'
                            '\n5. Atras'
                        )
                    opt = int(input('Opcion: '))
                    if opt == 1:
                        print(Fore.BLUE + 'Color azul')
                    elif opt == 2:
                        print(Fore.RED + 'Color rojo')
                    elif opt == 3:
                        print(Fore.MAGENTA + 'Color magenta')
                    elif opt == 4:
                        print(Fore.GREEN + 'Color verde')
                    elif opt == 5:
                        continue
                    else:
                        print('Escoja una opcion valida.')

                elif opt == 2:
                    continue
                else:
                    print('Escoja una opcion valida.')
            elif opt == 4:
                break
            else:
                print('Escoja una opcion valida.')
ru = Menu()
ru.run()