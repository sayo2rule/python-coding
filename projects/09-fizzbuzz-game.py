# FizzBuzz game
print("Welcome to the FizzBuzz Game!")
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")  # Print "FizzBuzz" for numbers divisible by both 3 and 5
    elif number % 3 == 0:
        print("Fizz")  # Print "Fizz" for numbers divisible by 3
    elif number % 5 == 0:
        print("Buzz")  # Print "Buzz" for numbers divisible by 5
    else:
        print(number)  # Print the number itself if it's not divisible by 3 or 5