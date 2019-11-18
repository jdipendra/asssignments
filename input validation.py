
#program starts here


import sys
# This is the start of the code that accept the user detail and  checks the validity of them.
name = input("Enter your name:\n")
for x in range(1, 5):
    if name.isalpha() == True or ' ' in name:
        if len(name) >=3:
            print("You entered the name:", name)
            break
        else:
            print("Invalid input!!!\nName must be more than two alphabets!")
            name = input("Enter your name again:\n")
    else:
        print("Invalid name!!!\nName must alphabets!")
        name = input("Enter your name again:\n")
print("\nNow time for age verification:")

age = input("Enter your age:")
for y in range(1, 5):
    if age.isdecimal() == True:
        if int(age) >=18:
            if len(age)<=2:
                print("You entered the age:\n", age)
                break
            else:
                print("Only two digits age is valid.\n")
                age = input("Enter your age again:\n")
        else:
            print("Invalid input!!!\nAge must be more than 18 years to be able to use this application!")
            age = input("Enter your age again:\n")
    else:
        print("Invalid input!!!\nAge must be decimal value!")
        age = input("Enter your age again:\n")
print("\nNow time to give your mobile number:")

mobile_no =  input("Enter your mobile number:\n")
for z in range(1, 5):
    if mobile_no.isdecimal() == True:
        if len(mobile_no) ==10:
            print("Your mobile number:", mobile_no)
            break
        else:
            print("Invalid input!!!\nMobile number must be 10 digit long!")
            mobile_no = input("Enter your mobile number again:")
    else:
        print("Invalid input!!!\nMobile number must be decimal value!")
        mobile_no = input("Enter your mobile number again:")
print("You entered the following entries\nName          :", name, "\nAge           :",
      age, "\nMobile number :", mobile_no,)
#personal detail input and verification ends here