def get_last_element(lst):
    print(lst[len(lst) - 1])
    
def get_lst():
    lst = []
    str = input("Enter the element of list: ")
    while str != "":
        lst.append(str)
        str = input("Enter the element of list: ")
    return lst

def main():
    lst = get_lst()
    if lst:
        get_last_element(lst)
    else:
        print("list ie empty")
        
main()