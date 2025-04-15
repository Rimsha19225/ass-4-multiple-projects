import random

print("Wellcome to Password Generator Application")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*?+-0123456789"

number = int(input("Enter amount of password: "))
length = int(input("Enter how long pasword length: "))

print("\nhere are your passwords: ")

for password in range(number):
    passwords = ""
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)