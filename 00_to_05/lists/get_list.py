def get_lst(lst):
    print("The list element is ", lst)


def get_list():
    lst = []
    str = input("Enter the element of list: ")
    while str != "":
        lst.append(str)
        str = input("Enter the element of list: ")
    return lst

def main():
    lst = get_list()
    if lst:
        get_lst(lst)
    else: 
        print("the string is empty")
        
main()