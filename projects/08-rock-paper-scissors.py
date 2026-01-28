# Rock, paper, scissors game
import random
print("Welcome to the Rock, Paper, Scissors Game!")
user_option = input("Choose Rock, Paper, or Scissors: ").capitalize()
options = ["Rock", "Paper", "Scissors"]
computer_option = random.choice(options)
print(f"Computer chose: {computer_option}")
if user_option == computer_option:
    print("It's a tie!")
elif (user_option == "Rock" and computer_option == "Scissors") or \
     (user_option == "Paper" and computer_option == "Rock") or \
     (user_option == "Scissors" and computer_option == "Paper"):
    print("You win!")
else:
    print("You lose!") 
