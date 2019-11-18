def f_palindrome(n):
    rev_number = 0
    while n > 0:
        num = n%10
        rev_number = int(rev_number) * 10 + num
        n=int(n/10)
    return rev_number
number = int(input("Enter the number to check whether it is a pallindrome:\n"))
pal = f_palindrome(number)
if pal == number:
    print(number, "ia Palindrome.")
else:
    print(number, "is not palindrome.")