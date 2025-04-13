max_length = 3

def shorten(lst): 
    while len(lst) > max_length:
        last_elem = lst.pop()
        print(last_elem)
        
def get_list():
    lst = []
    str = input("Enter the element of list: ")
    while str != "":
        lst.append(str)
        str = input("Enter the element of list: ")
    return lst

def main():
    lst = get_list()
    shorten(lst)
    
main()