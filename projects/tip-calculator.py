# Welcome to Tip Calculator.
print("Welcome to the Tip Calculator.")
# Get the total bill amount
bill = float(input("What was the total bill? $"))
# Get the tip percentage
tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
# Get the number of people to split the bill
num_people = int(input("How many people to split the bill? "))
# Calculate the total tip amount
tip_amount = bill * (tip_percentage / 100)
# Calculate the total bill including tip
total_bill = bill + tip_amount
# Calculate the amount each person should pay
amount_per_person = total_bill / num_people
# Format the amount to 2 decimal places
final_amount = "{:.2f}".format(amount_per_person)
# Print the final amount each person should pay
print(f"Each person should pay: ${final_amount}")   