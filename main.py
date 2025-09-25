


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
def main():
    print('Main function is working!')

#endregion


#region MAIN PROGRAM
main()
#endregion
