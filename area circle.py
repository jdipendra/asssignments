#area of circle
def area_of_circle(r):
    area = 22/7*r*r
    return area
radius = input("Enter the value of Radius:\n")
area = area_of_circle(float(radius))
print("Area of circle with radius", radius, "i=", area)