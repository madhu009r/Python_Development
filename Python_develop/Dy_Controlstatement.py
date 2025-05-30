#Control Statment

#Example in movie ticket price
ticket_price =90
wallet_size =100

#comparison <,>,<=,>=,==,!=
if ticket_price <= wallet_size:
    print("Hurray, I can go to this movie!")
else:
    print("Sad, i don't have enough purse")

#nested
# if elif else
# checking a leap year

year=int(input("Enter the year: "))

if(year % 4 == 0 and year %100 !=0 ) or (year%400==0):
    print("Leap year")
else:
    print("Not leap year")

# working with grade system
marks = float(input("Enter your marks: "))
if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 50:
    print("D")
else:
    print("Fail")

# Determine the type of triangle based on sides:
    side1 = float(input("Enter side 1: "))
    side2 = float(input("Enter side 2: "))
    side3 = float(input("Enter side 3: "))
    
    if side1 == side2 == side3:
        print("Equilateral")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("Isosceles")
    else:
        print("Scalene")
# Number Range

num = int(input("Enter a number: "))  
if num > 0:
    print("Positive")
    if num > 100:
        print("Greater than 100")
    else:
        print("Within 1 to 100")
elif num < 0:
    print("Negative")
else:
    print("Zero")