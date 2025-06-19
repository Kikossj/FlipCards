







while True:
            print('¿Que quieres hacer?')
            print(
                '1. Crear tarjeta' '\n2. Ver tarjetas'
                '\n3. Crear mazo' '\n4. Ver mazos'
                '\n5. Cambiar el color de el menu' '\n6. Eliminar mazo'
                '\n7. Salir'
            )
            opt = int(input('Opción: '))
            if opt == 1:
                title = input('Ingrese titulo: ')
                desc = input('Ingrese descripcion: ')
                cards = Card(title, desc)
                cards.add_card()
            elif opt == 2:
                cards = Card()
                cards.load_card()
            elif opt == 3:
                title = input("Elige un nombre para el mazo: ")
                decks = Deck(title)
                decks.add_deck()
            elif opt == 4:
                decks = Deck()
                decks.load_deck_data()
            elif opt == 5:
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
            elif opt == 6:
                cards = Card()
                cards.remove_card()
            elif opt == 7:
                break
