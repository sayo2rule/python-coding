# Loops; For loops; While loops; Range; Code blocks
# For loops
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # Print each fruit in the list
    print(fruit + " is delicious!")  # Print a message for each fruit

# Example of a for loop with a range
student_scores = [85, 92, 78, 90, 88, 95, 80, 91, 89, 94, 87, 93, 82, 96, 84, 90, 91, 88, 89, 92]
total_exam_score = sum(student_scores)
print(f"Total exam score: {total_exam_score}")  # Print the total exam score

sum = 0    
for score in student_scores:
    sum += score  # Add each score to the total sum
print(f"Total exam score: {sum}")  # Print the total exam score

# Add 1 - 100 using a for loop and range
total_sum = 0
for number in range(1, 101):
    total_sum += number  # Add each number to the total sum
print(f"Total sum from 1 to 100: {total_sum}")  # Print the total sum from 1 to 100

range(1, 101)  # Create a range object from 1 to 100
print(list(range(1, 101)))  # Print the list of numbers from 1 to 100

# Carl Gauss
gauss_sum = sum(range(1, 101))  # Calculate the sum from 1 to 100 using the sum function
print(f"Gauss's sum from 1 to 100: {gauss_sum}")  # Print Gauss's sum from 1 to 100


