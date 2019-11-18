year = int(input("Enter year to check whether it is a leap year:\n"))
if year%400 == 0:
    print("The year you entered:", year, ", is a leap year.")
elif year%4 == 0 and year%100 != 0:
    print("The year you entered:", year, ", is a leap year.")
else:
    print("The year you entered:", year, ", is not a leap year.")