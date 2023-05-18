import datetime

def start_working_day(name, family_name):
    Pradzia = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("Pradzia.txt", "a") as file:
        file.write(f"{name},{family_name},{Pradzia}\n")

    print("Darbo diena prasidejo!")


def end_working_day(name, family_name):
    start_time = None
    end_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("Pradzia.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == name and data[1] == family_name:
                start_time = data[2]
                break

    if start_time is None:
        print("Darbo diena nebuvo pradeta.")
        return

    start_datetime = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_datetime = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    working_time = end_datetime - start_datetime

    with open("Pabaiga.txt", "a") as file:
        file.write(f"{name},{family_name},{start_time},{end_time},{working_time}\n")

    print("Baigei darbo diena!")
    print(f"Is viso dirbo: {name} {family_name}", working_time)

def darbas(name, family_name):
    if name is not None and family_name is not None:
        while True:
            print("\nMenu:")
            print("1. Pradeti darbo diena")
            print("2. Baigti darbo diena")
            print("3. Atsijungiama")

            option = input("Ka norite daryti?: ")

            if option == "1":
               start_working_day(name, family_name)
            elif option == "2":
              end_working_day(name, family_name)
            elif option == "3":
                print("Atsijungiama...")
                menu()
            else:
                print("Blogai ivestas pasirinkimas.")

def register():
    name = input("Iveskite varda: ")
    family_name = input("Iveskite pavarde: ")
    email = input("Iveskite email: ")
    phone = input("Iveskite telefono numeri: ")
    username = input("Iveskite slapyvardi: ")
    password = input("Iveskite slaptazodi: ")

    with open("Duomenys.txt", "a") as file:
        file.write(f"{name},{family_name},{email},{phone},{username},{password}\n")

    print("Registracija sekminga!")


def login():
    username = input("Iveskite slapyvardi: ")
    password = input("Iveskite slaptazodi: ")

    with open("Duomenys.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[4] == username and data[5] == password:
                print("Sekmingai prisijungete\n")
                name = data[0]
                family_name = data[1]
                darbas(name, family_name)
                return

    print("Neteisingi prisijungimo duomenys.")

def menu():
    print("\n1. Registruotis \n2. Prisijungti")
    choise =input()
    if choise == '1':
        register()
    elif choise == '2':
        login()
    else:
        print("Blogai ivesti duomenys")
        return
# Test the functions


menu()