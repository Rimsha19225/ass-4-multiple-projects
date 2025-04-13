

def fruit_cost():
    dic = {
    "apple" : 50,
    "banana" : 30,
    "mango" : 35,
    "kiwi" : 50,
    "orange" : 30,
    "watermelon": 35,
    "dates" : 25,
    "sugercane" : 30
    }
    total_price = 0
    for fruit in dic:
        price = dic[fruit]
        buy_price = int(input("How many (" + fruit +") do you want?: "))
        total_price += price * buy_price
    print(f"Your total price is: ${total_price}")


fruit_cost()