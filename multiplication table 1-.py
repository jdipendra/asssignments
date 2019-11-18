import sys
looping ='y'
while(looping =='y' or looping == 'Y'):
    number = int(input("\neneter number whose multiplication table you want to print\n"))
    for i in range(1,11):
        print(number, "x", i, "=", number*i)
    else:
        looping = input("\nDo you want to print another table?\npress Y/y for yes and press any key to exit program.\n")
        if looping =='y' or looping == 'Y':
            looping = looping
        else:
            sys.exit("program exiting.......")
