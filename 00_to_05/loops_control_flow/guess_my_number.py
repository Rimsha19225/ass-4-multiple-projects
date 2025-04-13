import random

def number_guess():
    secret_number = random.randint(0, 99)
    print("welcome to guess game....")
    guess_number = int(input("Enter the guess number: "))
    while secret_number != guess_number:
        if guess_number < secret_number:
            print("Your Guess is low")
        else:
            print("Your Guess is high")
        guess_number = int(input("Enter again guess number: "))
    
    print(f"Congratulation the guess number is correct {secret_number}")
    
number_guess()