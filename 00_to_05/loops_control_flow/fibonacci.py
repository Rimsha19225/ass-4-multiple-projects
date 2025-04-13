max_term_value = 10000


def fib():
    current_value = 0
    next_value = 1
    while current_value <= max_term_value:
        print(current_value)
        after_next_value = current_value + next_value
        current_value = next_value
        next_value = after_next_value


fib()