first_side = input("Enter the first side of the quadrilateral:\n")
second_side = input("Enter the second side of the quadrilateral:\n")
third_side = input("Enter the third side of the quadrilateral:\n")
forth_side = input("Enter the forth side of the quadrilateral:\n")
if float(first_side) != float(second_side) and float(first_side) != float(third_side) and float(first_side) != float(forth_side):
    print("The Geometric figure is an irregular shaped Quadrilateral.")
elif float(first_side) == float(third_side) and float(second_side) == float(forth_side) and float(first_side) != float(second_side):
    digonal1 = input("Enter first digonal:\n")
    digonal2 = input("Enter second digonal:\n")
    if float(digonal1) == float(digonal2):
        print("The Geometric figure is a rectangle.")
    else:
        print("The Geometric figure is a parallelogram.")
elif float(first_side) == float(second_side) == float(third_side) == float(forth_side):
    digonal1 = input("Enter first digonal:\n")
    digonal2 = input("Enter second digonal:\n")
    if float(digonal1) == float(digonal2):
        print("The Geometric figure is a square.")
    else:
        print("The Geometric figure is a rhombus.")