# While loop
# A while loop is a control flow statement that allows code to be executed repeatedly based on a given boolean condition. The code inside the loop will continue to execute as long as the condition is true.

# Example of a while loop that counts from 1 to 5
count = 1  # Initialize the count variable
while count <= 5:  # Loop condition: continue as long as count is less than or equal to 5
    print(count)  # Print the current value of count
    count += 1  # Increment the count variable by 1
# Output:
# 1
# 2
# 3
# 4
# 5 

# Example of a while loop that calculates the factorial of a number
number = 5  # The number for which we want to calculate the factorial
factorial = 1  # Initialize the factorial variable
while number > 1:  # Loop condition: continue as long as number is greater than 1
    factorial *= number  # Multiply the current value of factorial by number
    number -= 1  # Decrement the number variable by 1
print(factorial)  # Output: 120 (5! = 5 * 4 * 3 * 2 * 1)    

# Example of a while loop that prompts the user for input until they enter 'exit'
user_input = ""  # Initialize the user_input variable
while user_input.lower() != "exit":  # Loop condition: continue until the user enters 'exit' (case-insensitive)
    user_input = input("Enter something (type 'exit' to quit): ")  # Prompt the user for input
    print(f"You entered: {user_input}")  # Print the user's input
# Output:
# Enter something (type 'exit' to quit): Hello
# You entered: Hello
# Enter something (type 'exit' to quit): exit
# You entered: exit 

# Example of a while loop that generates the Fibonacci sequence up to a certain number
a, b = 0, 1  # Initialize the first two numbers in the Fibonacci sequence
while a <= 100:  # Loop condition: continue as long as a is less than or equal to 100
    print(a)  # Print the current value of a
    a, b = b, a + b  # Update a to be b and b to be the sum of a and b
# Output:
# 0
# 1
# 1                     

# Example of a while loop that simulates a simple guessing game
import random  # Import the random module to generate a random number
number_to_guess = random.randint(1, 10)  # Generate a random number between 1 and 10
guess = None  # Initialize the guess variable
while guess != number_to_guess:  # Loop condition: continue until the user guesses the correct number
    guess = int(input("Guess a number between 1 and 10: "))  # Prompt the user for a guess and convert it to an integer
    if guess < number_to_guess:  # Check if the guess is too low
        print("Too low! Try again.")  # Inform the user that their guess is too low
    elif guess > number_to_guess:  # Check if the guess is too high
        print("Too high! Try again.")  # Inform the user that their guess is too high
    else:
        print("Congratulations! You guessed the number!")  # Inform the user that they guessed correctly
# Output:
# Guess a number between 1 and 10: 5
# Too low! Try again.
# Guess a number between 1 and 10: 8
# Too high! Try again.
# Guess a number between 1 and 10: 7
# Congratulations! You guessed the number!      