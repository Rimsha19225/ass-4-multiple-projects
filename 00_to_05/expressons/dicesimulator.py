import random


def roll_die():
    for i in range(1, 4):
        print("Rolling the dice...")
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"Die 1: {die1} and Die 2: {die2}")
        print(f"Total: {die1 + die2}")

roll_die()
