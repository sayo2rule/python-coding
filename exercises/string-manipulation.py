# print() function
print("Hello world!") #Strings of character

# Multiline string
print(
    """
  1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.
  2. Knead the dough for 10 minutes.
  3. Add 3g of Salt.
  4. Leave to rise for 2 hours.
  5. Bake at 200 degrees C for 30 minutes.
    """
)

# \n new line
print("Hello\nWorld!")

# String concatenation
print("Hello" + " World!")

# String repetition
print("Hello " * 3) # Hello Hello Hello

# String indexing
greeting = "Hello"
print(greeting[0])  # H
print(greeting[1])  # e
print(greeting[2])  # l
print(greeting[3])  # l
print(greeting[4])  # o     

# String slicing
print(greeting[0:2])  # He
print(greeting[2:5])  # llo
print(greeting[:3])   # Hel
print(greeting[3:])   # lo

# String length
print(len(greeting))  # 5

# input() function
name = input("What is your name: ")
print("Hello " + name)

# f-strings
age = 25
print(f"My name is {name} and I am {age} years old.")

# String methods
text = "  Hello World!  "
print(text.lower())        # hello world!
print(text.upper())        # HELLO WORLD!
print(text.strip())       # "Hello World!"
print(text.replace("World", "There"))  # "  Hello There!  "
print(text.split())       # ['Hello', 'World!']
print(text.find("World")) # 8 (returns -1 if not found)   
print(text.count("l"))    # 3
print(text.startswith("  He")) # True
print(text.endswith("!  "))   # True  
print(text.isalpha())    # False (because of spaces and punctuation)
print(text.isdigit())    # False

# Escape characters
print("He said, \"Hello World!\"")  # He said, "Hello World!"
print('It\'s a beautiful day!')      # It's a beautiful day!
print("C:\\Users\\Name")             # C:\Users\Name  
print("First Line\nSecond Line")     # First Line
                                      # Second Line
print("Column1\tColumn2")           # Column1	Column2

# Variables in strings
city = "New York"
print(f"I live in {city}.")  # I live in New York.  
print("I live in {}.".format(city))  # I live in New York.  
print("I live in %s." % city)  # I live in New York.

# String formatting with width and precision
number = 3.14159
print(f"Number: {number:.2f}")      # Number: 3.14
print("Number: {:.2f}".format(number))  # Number: 3.14
print("Number: %0.2f" % number)     # Number: 3.14  

# Exercises
# We have 2 variables glass1 and glass2. 
# glass1 contains milk and glass2 contains juice. 
# Write 3 lines of code to switch the contents of the variables. 
# You are not allowed to type the words "milk" or "juice". 
# You are only allowed to use variables to solve this exercise.
glass1 = "milk"
glass2 = "juice"

temp = glass1
glass1 = glass2
glass2 = temp
print("glass1 contains:", glass1)  # glass1 contains: juice
print("glass2 contains:", glass2)  # glass2 contains: milk

# Given the string "Python is awesome",
# write code to extract and print the word "awesome" using string slicing.
text = "Python is awesome"
print(text[10:])  # awesome

# Write code to count the number of times the letter 'o' appears in the string "Hello World".
text = "Hello World"
print(text.count('o'))  # 2 

# Given the string "   Data Science   ",
# write code to remove the leading and trailing spaces and convert it to uppercase.
text = "   Data Science   "
cleaned_text = text.strip().upper()
print(cleaned_text)  # DATA SCIENCE

# Write code to check if the string "OpenAI" starts with the substring "Open" and ends with "AI".
text = "OpenAI"
starts_with_open = text.startswith("Open")
ends_with_ai = text.endswith("AI")
print("Starts with 'Open':", starts_with_open)  # Starts with 'Open': True
print("Ends with 'AI':", ends_with_ai)          # Ends with 'AI': True  