import random 

def guess():
    print("The number guess match start between user and computer...!")
    computer_guess = random.randint(0, 10)
    user_guess = int(input("Enter guess number: "))
    if computer_guess == user_guess:
        print("You win..😃")
    else:
        print("you loss..😑")
        
guess()