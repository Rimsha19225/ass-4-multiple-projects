affirmation = "I am capable, confident, and ready to achieve great things today."

def affirmation_fun():
    print("type the affirmation " + affirmation)
    
    user_data = input()
    while user_data != affirmation:
        print("the user is not affirmation")
        print("type the affirmation " + affirmation)
        user_data = input()
        
    print("it's right: ")
    
affirmation_fun()
        