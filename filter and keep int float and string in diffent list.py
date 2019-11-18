import sys
list = []
i=0
items = int(input("enter the number of items that you want in your list:\n"))
while i<items:
    print("enter item:")
    elements = input()
    list.append(elements)
    i+=1
integer = []
float = []
string = []
for i in list:
    if type(i)==int:
        integer.append(i)
    elif type(i)==float:
        float.append(i)
    else:
        string.append(i)
print("List of integer is:",integer, "\nList of float is:", float, "\nList of string is:",string)