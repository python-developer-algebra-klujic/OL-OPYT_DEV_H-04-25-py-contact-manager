import os


#region INITIAL DATA

contacts = [
    {
        'id': 1,
        'first_name': 'Pero',
        'last_name': 'Peric',
        'phone': '09x 1234 567',
        'email': 'pero.peric@email.hr'
    },
    {
        'id': 2,
        'first_name': 'Ana',
        'last_name': 'Anic',
        'phone': '09x 7654 321',
        'email': 'ana.anic@email.hr'
    },
    {
        'id': 3,
        'first_name': 'Mirko',
        'last_name': 'Mirkic',
        'phone': '09x 9513 579',
        'email': 'mirko.mirkic@email.hr'
    },
    {
        'id': 4,
        'first_name': 'Slavko',
        'last_name': 'Slavkic',
        'phone': '09x 3578 963',
        'email': 'slavko.slavkic@email.hr'
    },
]

customers = [
    {
        'id': 1,
        'name': 'Pajdo und Jaranen GmbH',
        'vat_id': '01234567890',
        'contacts': [1, 2]
    },
    {
        'id': 2,
        'name': 'The Best Software Ltd.',
        'vat_id': '98765432100',
        'contacts': [3, 4]
    }
]

#endregion


#region FUNCTIONS


#region GUI MODUL

def clear_display() -> None:
    os.system('cls')
    print('clear_display() is working')

def main_menu() -> int:
    while True:
        # Ocisti ekran -> funkcija clear_display()
        clear_display()

        print('main_menu() is working.')
        print('1. Test')
        print('0. Exit')

        meni_item = input('Upisite broj ispred funkcionalnosti koju zelite napraviti: ')

        if meni_item.isdigit():
            return int(meni_item)
        else:
            print('Neispravan unos! Pokusajte ponovno.')
            input('Za novi izbor pritisnite tipku ENTER.')




#endregion

#region CONTACTS MODUL

#endregion

#region CUSTOMERS MODUL

#endregion


def main():
    while True:
        # Prikazati izbornik -> funkcija main_menu()
        menu_item = main_menu()

        # Ovisno o izboru meni_item pozvati odgovarajucu funkciju
        if menu_item == 0:
            return
        else:
            print(menu_item)
            input()

#endregion


#region MAIN PROGRAM
if __name__ == '__main__':
    main()
#endregion
