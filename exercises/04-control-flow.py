# Control flow exercises
# If-else statement to check odd or even number
number = int(input("Which number do you want to check? "))
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

# Multiple if statements
new_number = int(input("Enter a number to see if it's divisible by 2, 3, 5, or 10: "))
if new_number % 2 == 0:
    print("This number is divisible by 2.")
if new_number % 3 == 0:
    print("This number is divisible by 3.")
if new_number % 5 == 0:
    print("This number is divisible by 5.")
if new_number % 10 == 0:
    print("This number is divisible by 10.")    

# Leap year checker
year = int(input("Enter a year to check if it's a leap year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")    


# Logical operators: and, or, not
a = 12  
a > 15 # False
a < 20 # True
a > 7 # True

a > 10 and a < 15 # True
a > 10 or a < 15 # True
a > 15 and a < 20 # False
a > 15 or a < 20 # True
not(a > 15) # True
not(a < 20) # False
not(a > 7) # False

# Combining conditions with logical operators
b = 7
if b > 5 and b < 10:
    print("b is between 5 and 10.")
if b < 5 or b < 10:
    print("b is less than 5 or less than 10.")
if not(b > 10):
    print("b is not greater than 10.")

# Exercises
a = 5
b = 7
 
if a >= b and a != b:
    print("A")
elif not a >= b and a != b:
    print("B")
else:
    print("C")
# Expected output: B

