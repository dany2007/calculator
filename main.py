import sqlite3
import pyinputplus
import calculator


def menu():
    my_menu = """Va rog alegeti optiunea corespunzatoare actiunii pe care vreti sa o indepliniti:
     1. Vedeti operatiile unui utilizator.
     2. Introduceti valori noi.
     3. Afisati toate intrarile existente        
     4. Folositi calculatorul 
    """
    print(my_menu)


def get_option():
    menu()
    optiune = input("Valoarea dorita:")
    return optiune


def input_data():
    nume = input("Va rog introduceti numele:")
    prenume = input("Va rog introduceti prenumele:")
    return nume, prenume


def alegere_tabel():
    tabele_disponibile = ['Operatii', 'utilizatori']
    tabel_ales = pyinputplus.inputMenu(tabele_disponibile,"Va rugam alegeti unul dintre tabelele disponibile: \n", numbered=True)
    return tabel_ales


while True:
    my_option = get_option()
    my_connection = sqlite3.connect('calculator.db')
    my_cursor = my_connection.cursor()

    if my_option == '1':
        name, surname = input_data()
        my_query = f"select * from Operatii where Id_client = (SELECT id from utilizatori where nume = '{name}' and Prenume = '{surname}')"

    elif my_option == '2':
        name, surname = input_data()
        my_query = f"INSERT INTO utilizatori(Nume,Prenume,Id) VALUES('{name}','{surname}',(select max(Id) from utilizatori) + 1 );"

    elif my_option == '3':
        tabel_ales = alegere_tabel()
        my_query = f"SELECT * FROM '{tabel_ales}';"

    elif my_option == '4':
        name, surname = input_data()
        my_query = f'SELECT id from utilizatori where prenume="{surname}" and nume="{name}";'
        my_cursor.execute(my_query)
        calculator.main(id_utilizator=my_cursor.fetchone()[0])
    else:
        print('alegeti o optiune valida')
        continue

    result = my_cursor.execute(my_query)
    # print(result.fetchall())

    for item in result.fetchall():
        if my_option == '1':
            message = f'{surname} {name} cu id ul unic {item[0]} a folosit aplicatia si a efectuat operatia ' \
                      f'corespunzatoare operatorului {item[1]} asupra numerelor {item[2]} si {item[3]} '
            print(message)
        elif my_option == '3':
            if tabel_ales == 'utilizatori':
                message = f'{item[1]} {item[2]} cu id-ul {item[0]}'
                print(message)
            elif tabel_ales == 'Operatii':
                message = f'Clientul cu id-ul {item[0]} a executat operatia {item[1]} pe numerele {item[2]} si {item[3]}'
                print(message)
            else:
                print("Va rugam alegeti un tabel valid")


    my_connection.commit()
    continuare = input("Do you want to continue (YES/no): ")
    if continuare.lower() == "no":
        break

my_connection.close()
print("Finished.")
