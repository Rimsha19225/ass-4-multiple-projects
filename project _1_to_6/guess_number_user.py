import random 

def guess():
    print("The number guess match start between user and computer...!")
    computer_score = 0
    user_score = 0
    computer_guess = random.randint(0, 10)
    user_guess = int(input("Enter guess number: "))
    rounds = 1
    while rounds <= 5:
        if computer_guess == user_guess:
            print(f"You Win round {rounds}")
            user_score = user_score + 1
            print(f"The user score is: {user_score} and computer score is: {computer_score}")
        else:
            print(f"You loss round {rounds}")
            computer_score = computer_score + 1
            print(f"The user score is: {user_score} and computer score is: {computer_score}")
        if rounds < 5:
            user_guess = int(input("Enter again guess number round: "))
        rounds = rounds + 1
    if user_score < computer_score:
        print("You loss the match and Computer win.")
        print("Try agin and do your best next time.")
    elif user_score == computer_score:
        print("The match tie both score equal.")
    else:
        print("You win the match and Computer loss.")
        print("Congratulations...!")
        
guess()