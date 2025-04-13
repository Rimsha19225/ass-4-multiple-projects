vote_age = int(input("How old are you? "))
if vote_age < 16:
    print(f"I am {vote_age} years old.")
    print("You are not eligible to vote cast in any country.")
elif vote_age < 25:
    print(f"I am {vote_age} years old.")
    print("You can vote in Peturksbouipo where the voting age is 16.")
elif vote_age < 48:
    print(f"I am {vote_age} years old.")
    print("You can vote in Peturksbouipo where the voting age is 16. You can also vote in Stanlau where the voting age is 25.")
elif vote_age > 48:
    print(f"I am {vote_age} years old.")
    print("You can vote in Peturksbouipo where the voting age is 16. You can vote in Stanlau where the voting age is 25. You can also vote in Mayengua where the voting age is 48.")
else:
    print("invalid age enter")