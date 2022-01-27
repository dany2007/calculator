import sqlite3


def main(id_utilizator):
    rezultat = []
    my_connection = sqlite3.connect('calculator.db')
    my_cursor = my_connection.cursor()

    while True:
        input_type = input("Doriti input din prompt[1] sau din fisier[2]: ")
        if input_type == "1" or input_type == "2":
            break
        else:
            print("Va rog sa introduceti o optiune valida")

    if input_type == "1":
        while True:
            operatie = ["", "", ""]
            operatie[0] = input("Va rog introduceti primul numar: ")
            operatie[2] = input("Va rog introduceti al 2-lea numar: ")
            operatie[1] = get_operation()
            rezultat.append(do_math("".join(operatie)))
            my_query = f"INSERT INTO Operatii VALUES('{id_utilizator}','{operatie[1]}','{operatie[0]}','{operatie[2]}');"
            my_cursor.execute(my_query)
            my_connection.commit()
            my_connection.close()
            continuare = input("Do you want to continue (YES/no): ")
            if continuare.lower() == "no":
                print(rezultat)
                break

    if input_type == "2":
        while True:
            with open("input.txt") as fisier:
                for line in fisier.readlines():
                    rezultat.append(do_math(line))
                    db_operations = process_strings(line)
                    my_query = f"INSERT INTO Operatii VALUES('{id_utilizator}','{db_operations[2]}','{db_operations[0]}','{db_operations[1]}');"
                    my_cursor.execute(my_query)

            my_connection.commit()
            my_connection.close()
            print(rezultat)
            break


def process_strings(line):
    if "+" in line:
        line = line.strip().replace(" ", "").split("+")
        operator = "+"
    elif "*" in line:
        line = line.strip().replace(" ", "").split("*")
        operator = "*"
    elif "/" in line:
        line = line.strip().replace(" ", "").split("/")
        operator = "/"
    elif "-" in line:
        line = line.strip().replace(" ", "").split("-")
        operator = "-"
    else:
        operator = "Wrong Operator"

    if check_if_numbers(line[0], line[1]):
        return [int(line[0]), int(line[1]), operator]
    else:
        return [line[0], line[1], "NaN"]


def do_math(line):
    line = process_strings(line)
    if line[2] == "Wrong Operator":
        return "Wrong Operator"
    elif line[2] == "NaN":
        return "NaN"
    elif line[2] == "+":
        return int(line[0]) + int(line[1])
    elif line[2] == "*":
        return int(line[0]) * int(line[1])
    elif line[2] == "/":
        if line[1] == "0":
            return "Div/0"
        else:
            return int(line[0]) / int(line[1])
    elif line[2] == "-":
        return int(line[0]) - int(line[1])


def check_if_numbers(numar1, numar2):
    if not numar1.isnumeric():
        return False
    if not numar2.isnumeric():
        return False
    return True


def get_operation():
    while True:
        simbol_ales = input("Avem urmatoarele optiuni:\n"
                            "1) \'Adunare\'(+) \n"
                            "2) \'Inmultire\'(*)\n"
                            "3) \'Impartire\'(/) \n"
                            "4) \'Diferenta\'(-) \n"
                            "Va rog introduceti optiunea (semnul operatiei): ")
        if simbol_ales == '+' or simbol_ales == '*' or simbol_ales == '/' or simbol_ales == '-':
            break
        else:
            print("\nVa rugam sa alegti un semn valid\n")
    return simbol_ales


if __name__ == "__main__":
    main(1)
