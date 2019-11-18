#power of number
def pow(a,b):
    power = a**b
    return power
base = input("Enter base of the exponential:\n")
exponent = input("Enter exponent of the exponential:\n")
power = pow(float(base), float(exponent))
print("The value of the exponential with base", base,"and exponent", exponent,"is", power)