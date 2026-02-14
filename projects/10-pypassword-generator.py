# PyPassword Generator
import random
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!#$%&()*+'

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))
password_list = []
for _ in range(nr_letters):
    password_list.append(random.choice(letters))  # Add a random letter to the password list
for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))  # Add a random symbol to the password list
for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))  # Add a random number to the password list
random.shuffle(password_list)  # Shuffle the password list to randomize the order of characters
password = ''.join(password_list)  # Join the characters in the password list to create the final password string
print(f"Your generated password is: {password}")  # Print the generated password to the user    

