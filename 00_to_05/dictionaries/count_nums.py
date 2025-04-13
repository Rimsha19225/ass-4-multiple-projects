def get_user_number():
    lst = []
    while True:
        number = input("Enter a number (or press Enter to stop): ")
        if number == "":
            break
        lst.append(number)
    return lst


def count_num(lst):
    dic = {}
    for num in lst:
        if num not in dic:
            dic[num] = 1
        else:
            dic[num] += 1
    return dic


def count_print(dic):
    for num in dic:
        print(f"{num} appears {dic[num]} times.")


def main():
    user_nums = get_user_number()
    counts = count_num(user_nums)
    count_print(counts)


main()
