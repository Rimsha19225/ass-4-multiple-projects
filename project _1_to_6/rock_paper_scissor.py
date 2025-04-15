import random

print("wellcome to rock paper scissor game..!")
computer_data = (random.choice([1, 0, -1]))

keys = {
    "r" : 1,
    "p" : 0,
    "s" : -1
}



def game():
    rounds = 1
    user_score = 0
    computer_score = 0
    user_data = input("tell (r, p, s): ")   
    while rounds <= 5:
        print(f"Round: {rounds}")
        if user_data =="r" and computer_data == 1:
            print("you tie")   
            print(f"Your score: {user_score} and Computer score: {computer_score}")
        elif user_data =="r" and computer_data == 0:
            print("You loss")
            computer_score = computer_score + 1
            print(f"Your score: {user_score} and Computer score: {computer_score}")
        elif user_data =="r" and computer_data == -1:
            print("You win")
            user_score = user_score + 1
            print(f"Your score: {user_score} and Computer score: {computer_score}")
        elif user_data =="p" and computer_data == 1:
            print("You win")
            user_score = user_score + 1
            print(f"Your score: {user_score} and Computer score: {computer_score}")
        elif user_data =="p" and computer_data == 0:
            print("you tie")   
            print(f"Your score: {user_score} and Computer score: {computer_score}")
        elif user_data =="p" and computer_data == -1:
            print("You loss")
            computer_score = computer_score + 1
            print(f"Your score: {user_score} and Computer score: {computer_score}")
        elif user_data =="s" and computer_data == 1:
            print("You loss")
            computer_score = computer_score + 1
            print(f"Your score: {user_score} and Computer score: {computer_score}")
        elif user_data =="s" and computer_data == 0:
            print("You win")
            user_score = user_score + 1
            print(f"Your score: {user_score} and Computer score: {computer_score}")
        elif user_data =="s" and computer_data == -1:
            print("you tie")   
            print(f"Your score: {user_score} and Computer score: {computer_score}") 
        rounds = rounds + 1
        if rounds <= 5:
            user_data = input("tell again (r, p, s): ")
            
    if user_score > computer_score:
        print("You Win..!")
    elif user_score == computer_score:
        print("Tie...!")
    else:
        print("You loss..!")
            
game()