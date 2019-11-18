def f_armstrong(n):
    sum = 0
    while n > 0:
        num = n%10
        sum = sum + num**3
        n=int(n/10)
    return sum


number = int(input("Enter a number to check whether it is armstrong:\n"))
check = f_armstrong(number)
if check == number:
    print("Armstron")
else:
    print("Not Armstrong")
