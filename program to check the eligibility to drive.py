#This program is to check whether s/he can drive or not on the basis of his age
age = input("Enter your age:\n")
if int(age) >=18:
    print("Your are", age, "years old.\nYou are eligible to Drive.")
else:
    print("Your are only", age, "years old.\nYou aren't eligible to Drive.")