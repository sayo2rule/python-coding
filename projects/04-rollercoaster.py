# Rollercoaster ride eligibility and ticket pricing
print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster!")

    # Nested if-else statements for age-based ticket pricing
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif 45 <= age <= 55: # elif age >= 45 and age <= 55:
        bill = 0
        print("Everything is going to be okay. Have a free ride on us!  ")
    else:
        bill = 12
        print("Adult tickets are $12.") 
    
    # Additional photo option
    photo = input("Do you want a photo taken? Y or N: ")
    if photo.upper() == "Y":
        bill += 3
        print("Your final bill is $" + str(bill) + ".")    

else:
    print("Sorry, you have to grow taller before you can ride.")