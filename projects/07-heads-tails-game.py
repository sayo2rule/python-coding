# Heads or Tails Game
import random       
print("Welcome to the Heads or Tails Game!")
user_choice = input("Choose Heads or Tails: ").lower()
random_choice = random.randint(0, 1)  # 0 for Heads, 1 for Tails
if random_choice == 0:
    computer_choice = "heads"
else:
    computer_choice = "tails"   
print(f"The computer chose: {computer_choice}")
if user_choice == computer_choice:
    print("You win!")
options = ["Rock", "Paper", "Scissors"]
computer_option = random.choice(options)
print(f"Computer chose: {computer_option}")
options = ["Rock", "Paper", "Scissors"]
user_option = input("Choose Rock, Paper, or Scissors: ").capitalize()
computer_option = random.choice(options)    