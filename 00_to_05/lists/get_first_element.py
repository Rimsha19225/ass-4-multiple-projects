def get_first_element(lst):
    print("First element of list is", lst[0])
    
    
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
        get_first_element(lst)
    else:
        print("List is empty.")
    
main()