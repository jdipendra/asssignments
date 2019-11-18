# This program will take list inputs form only one input statement
import sys
list = []
i = 0
print("this list is blank right now\nwe will make a list later")
print(list)
n = int(input("Enter number of elements:\Enter item of list.\nEnter item of the list."))
while(i<n):
    print("enter another item of the list")
    element = input()
    list.append(element)
    i+=1
print(list)
sys.exit("Program Exiting")