list = [3, 7, 2, 1, 4]
list.sort()
print("The orignal list is:", list)

for i in range(len(list)):
    a = list[i]
    list[i] = a * 2
    
print("The doubled list is:", list)
    