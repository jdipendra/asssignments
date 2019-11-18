marks = int(input("Enter the mark you get:"))
if marks <= 100 and marks >= 90:
    print("Grade-'A+'")
elif marks < 90 and marks >=80:
    print("Grade - 'A'")
elif marks < 80 and marks >=70:
    print("Grade - 'B+'")
elif marks < 70 and marks >= 60:
    print("Grade - 'B'")
elif marks < 60 and marks >= 50:
    print("Grade-'C+'")
elif marks < 50 and marks >= 40:
    print("Grade-'C'")
elif marks < 40 and marks >= 30:
    print("Grade-'D+'")
elif marks < 30 and marks >= 20:
    print("Grade-'D'")
elif marks < 20 and marks >= 10:
    print("Grade-'E+'")
else:
    print("Grade-'E'")