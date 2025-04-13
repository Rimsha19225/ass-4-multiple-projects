def read_phone_num():
    phonebook = {}
    while True:
        name = input("Name: ")
        if name == "":
            break
        number = int(input("Number: "))
        phonebook[name] = number
    return phonebook

def print_phonebook(phonebook):
    for name in phonebook:
        print(name + "  ->  " + str(phonebook[name]))
        
def look_num(phonebook):
    while True:
        name = input("Enter name to see")
        if name == "":
            break
        if name not in phonebook:
            print(name + " is not in the phonebook")
        else:
            print(phonebook[name])
            
            
def main():
    phonebook = read_phone_num()
    print_phonebook(phonebook)
    look_num(phonebook)

main()