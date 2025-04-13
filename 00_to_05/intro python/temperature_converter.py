print("Fahrenheit to Celsius Converter")
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0
celsius = fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit} Fahrenheit is equal to {celsius:.2f} Celsius")