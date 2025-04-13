JOKE = ("""Why don’t programmers like nature?
— It has too many bugs.""")
SORRY = "Sorry I only tell jokes"

user_input = input("What do you want? ")

if user_input.lower() == "joke":
    print(JOKE)
else:
    print(SORRY)