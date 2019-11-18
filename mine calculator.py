
import sys
menu = True
def calculator():
    print("You can do the following mathematical operations with BRILLIANT-CALCLATOR APP")
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Square Root\n6.Square\n7.Exponential\n8.nth Root")
    choice = int(input("Enter Your choice"))
    condition = 'Y'
    while condition == 'Y':
        if choice == 1:
            print("You choose an Addition.\nNow enter the entries which you want to add together:")



        elif choice == 2:
            print("You choose a Subtraction.\nNow enter the entries which you want to subtract:")





        elif choice == 3:
            print("You choose a Multiplication.\nNow enter the entries which your want to multiply together:")




        elif choice == 4:
            decision = 1
            while decision == 1:
                divident = input("enter Divident:\n\t")
                divisor = input("Enter Divisor:\n\t")
                result = int(divident) / int(divisor)
                reminder = int(divident) % int(divisor)
                print("\nResult of the division operation:\n\tquotent       :", int(result), "\n\treminder      :",
                      reminder)
                print("Do you want to divide another number?\n")
                decision = input("What you want to do?\n\t1.Menu\n\t2.Division\n\t3.Exit program\n")
                if decision == 1:
                    calculator()
                elif decision == 2:
                    decision = decision
                elif decision == 3:
                    decision = 0
                sys.exit("---------Program Exiting after division operation!!!---------")




        elif choice == 5:
            print("You choose to calculate the Square Root.\nEnter the number whose Square Root you want to calculate:")
            number = input("enter the number whose square root is to be calculated:\n")
            result = print("nth root:", float(number) ** (1 / float(2)))



        elif choice == 6:
            print("You choose to calculate Square of a number.\nEnter a number whose Square you want  to calculate:")
            number = input("enter the number whose nth root is to be calculated:\n")
            result = print("nth root:", float(number) ** (float(2)))



        elif choice == 7:
            print("You choose to calculate exponential value.\nEnter base and exponent:")

            base = (input("Enter base"))
            exponent = (input("Enter exponent of base"))

            result = print("The base ", base, "and exponent", exponent, "returned the value",
                           float(base) ** float(exponent))



        elif choice == 8:
            print("You choose to calculate nth root of the number.\nEnter the nht value of root and a number:")




        elif choice == 9:
            print(
                "You choose to calculate average value of the number.\nEnter numbers whose average you want to calculate:")
            list = []
            i = 0

            n = int(input("Enter number of elements whose Average you want to calculate:"))
            while (i < n):
                print("enter another item of the list")
                element = float(input())
                list.append(element)
                i += 1
            print(list)
            sum = 0
            for item in range(0, len(list)):
                sum = sum + list[item]
            print("The average of the numbers is:", sum / n)
            sys.exit("Program Exiting")




        elif choice == 10:
            print("You choose to calculate nth root of the number:")
            number = input("enter the number whose nth root is to be calculated:\n")
            nth_root = input("enter the nth root value")
            result = print("nth root:", float(number) ** (1 / float(nth_root)))



        else:
            print("Invalid input!!!")
            condition = 'f'

    sys.exit("\nThank you for using BRILLIANT-CALCULATOR APP\nprogram exiting.....")
calculator()