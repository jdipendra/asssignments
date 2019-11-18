#This program will filter the even number from the list of the number
import sys
list = []
i = 0
print("this list is blank right now\nwe will make a list later")
print(list)
n = int(input("Enter number of elements:\Enter item of list."))
while(i<n):
    print("enter item of the list")
    element = int(input())
    list.append(element)
    i+=1
print("list of items you entered is:")
print(list)

#this is the block of code that will filter even number from the list
output = []     #initialization of output list
for i in list:
    if i%2 == 0:
        output.append(i)
else:
    print("filtering the even number from the list has been done.\nThe list of even number is:", output)
sys.exit("Program Exiting")