def double(n):
    while n < 100:
        n *= 2
        print(n, end=' ')

user_input = int(input("Enter number to double: "))
double(user_input)