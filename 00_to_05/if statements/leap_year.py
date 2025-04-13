check_leap_year = int(input("Enter year to check leap or not: "))

if check_leap_year % 4 == 0:
    if check_leap_year % 100 == 0:
        if check_leap_year % 400 == 0:
            print("This is leap year.")
        else:
            print("Not a leap year!")
    else:
        print("This is leap year.")
else:
    print("Not a leap year!")