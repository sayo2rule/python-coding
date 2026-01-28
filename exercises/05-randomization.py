import random

# Random range
random_range = random.randrange(1, 10, 2)
print(random_range)     # Print a random odd integer between 1 and 9

random_range_20 = random.randrange(20)
print(random_range_20)  # Print a random integer between 0 and 19

# Random integer
random_integer = random.randint(1, 10)
print(random_integer)   # Print a random integer between 1 and 10 (inclusive)

# Random float
random_float = random.random()
print(random_float)     # Print a random float between 0.0 and 1.0

# Random float between 0 and 5
random_float_0_to_5 = random.random() * 5
print(random_float_0_to_5)  # Print a random float between 0.0 and 5.0

# Random uniform float between 1 and 10
random_uniform_float = random.uniform(1, 10)
print(random_uniform_float)  # Print a random float between 1.0 and 10.0

# Random triangular float between 1 and 10 with mode at 5
random_triangular_float = random.triangular(1, 10, 5)
print(random_triangular_float)  # Print a random float between 1.0 and 10.0 with mode at 5.0

# Random betavariate float with alpha=2 and beta=5
random_betavariate_float = random.betavariate(2, 5)
print(random_betavariate_float)  # Print a random float from a beta distribution

# Random expovariate float with lambda=1.5
random_expovariate_float = random.expovariate(1.5)
print(random_expovariate_float)  # Print a random float from an exponential distribution

# Random choice from a list
fruits = ["apple", "banana", "orange", "grape", "mango"]
random_fruit = random.choice(fruits)
print(random_fruit)  # Print a random fruit from the list

# List
# States of America
states = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia",
          "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi",
          "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
          "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota",
          "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
random_state = random.choice(states)
print(random_state)  # Print a random state from the list

last_state = states[-1]
print(last_state)  # Print the last state in the list

first_state = states[0]
print(first_state)  # Print the first state in the list

# Change the value of an element in the list
states[0] = "New Delaware"
print(states[0])  # Print the modified first state in the list

# Add a new state to the list
states.append("Puerto Rico")
print(states[-1])  # Print the newly added state

# Extend the list with multiple new states
states.extend(["Guam", "U.S. Virgin Islands"])
print(states[-2:])  # Print the newly added states

# Banker Roulette
friends = ["Alice", "Bob", "Charlie", "David", "Eve"]
random_friend = random.choice(friends)
print(f"{random_friend} is going to buy the meal today!")  # Print the randomly

# Nested list
nested_list = [
    ["Alice", "Bob", "Charlie"],
    ["David", "Eve", "Frank"],
    ["Grace", "Heidi", "Ivan"]
]
random_person = random.choice(random.choice(nested_list))


# Exercises
# 1. Given the following list:
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# Which line of code will give you "Apples"?
print(fruits[2])  # Print "Apples" from the list
print(fruits[-5])  # Print "Apples" using negative indexing

# 2. Given the code below:
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
fruits[-1] = "Melons"
fruits.append("Lemons")
print(fruits)
# What do you think will be printed?
# The modified list with "Pears" replaced by "Melons" and "Lemons" added at the end

# 3. Given the code below:
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])
# What will be printed?
# Output: "Kale" (vegetables list at index 1, then "Kale" at index 1 of vegetables)
