AB = float(input("Enter the length of AB: "))
AC = float(input("Enter the length of AC: "))
BC= AB ** 2 + AC ** 2

def calculate_hypotenuse():
    print("Calculating the length of the hypotenuse...")
    print(f"AB: {AB} units")
    print(f"AC: {AC} units")
    print(f"BC: {BC} units")
    print(f"Length of BC: {round((BC**2), 2)} units")
    
calculate_hypotenuse()