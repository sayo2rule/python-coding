# Data types
# Strings
name = "Alice"
print(type(name))  # <class 'str'>  

# Subscripts
first_letter = name[0]
print(first_letter)  # A
last_letter = name[-1] #last character
print(last_letter)   # e
# Slicing
substring = name[1:4]
print(substring)     # lic


# Integers
# Integers (whole numbers)
age = 30
print(type(age))   # <class 'int'>  

# Large integers
big_number = 12_345_678_901_234
print(type(big_number))  # <class 'int'>
print(big_number)  # 12345678901234

# Floats
height = 5.7
print(type(height))  # <class 'float'>
# Float operations  
sum_height = height + 2.3
print(sum_height)  # 8.0

# Booleans
is_student = True
print(type(is_student))  # <class 'bool'>
# Boolean operations
is_adult = age >= 18
print(is_adult)  # True 

# NoneType
data = None
print(type(data))  # <class 'NoneType'> 

# Checking for None
if data is None:
    print("No data available")
else:
    print("Data found") 

# Exercises
# 1. Create a string variable with your favorite color and print it.
favorite_color = "Blue"
print(favorite_color)   

# 2. Create an integer variable with your birth year and print it.
birth_year = 1990
print(birth_year)

# 3. Create a float variable with your height in meters and print it.
height_meters = 1.75
print(height_meters)    

# 4. Create a boolean variable indicating if you are a student and print it.
is_student = False
print(is_student)

# 5. Create a NoneType variable and check if it is None, printing an appropriate message.
data = None
if data is None:
    print("No data available")
else:
    print("Data found") 

# 6. Create a string variable with your full name, then print the first and last letters using indexing.
full_name = "John Doe"
print(full_name[0])    # J
print(full_name[-1])   # e     

# 7. Create a substring from your full name containing only your first name using slicing and print it.
first_name = full_name[0:4]
print(first_name)      # John  

# 8. Create a boolean variable that checks if your birth year is greater than 2000 and print the result.
is_born_after_2000 = birth_year > 2000
print(is_born_after_2000)  # False 

# 9. Create a float variable that adds 5.5 to your height and print the result.
new_height = height_meters + 5.5
print(new_height)      # 7.25

# 10. Create a string variable that concatenates your first and last name and print it.
full_name_concatenated = "John" + " " + "Doe"
print(full_name_concatenated)  # John Doe   

# 11. What is the data type of the mystery variable?
mystery = 734_529.678
print(type(mystery))  # <class 'float'>

# I've put a spell on you. You are now a computer. 
# If I give you the following code, what will you print out?
street_name = "Abbey Road"
print(street_name[4] + street_name[7])
# The output will be "yo" because street_name[4] is 'y' and street_name[7] is 'o'.


# Type errors, casting and checking
# Type errors
# Uncommenting the following line will raise a TypeError
# result = "Age: " + 30

# Type casting; int(), float(), str(), bool()
age = 30
age_str = str(age)
print("Age: " + age_str)  # Age: 30 

height_str = "5.9"
height_float = float(height_str)
print(height_float + 1.1)  # 7.0

# Type checking
print(isinstance(age, int))      # True
print(isinstance(age_str, str))  # True 
print(isinstance(height_float, float))  # True
print(isinstance(is_student, bool))  # True

# Alternatively, using type()
print(type(age))      # <class 'int'>
print(type(age_str))  # <class 'str'>
print(type(height_float))  # <class 'float'>
print(type(is_student))  # <class 'bool'>

# Value errors
# Uncommenting the following line will raise a ValueError
# invalid_int = int("abc")
# invalid_float = float("xyz")
# invalid_bool = bool("maybe")  # This will not raise an error; 
# it will return True since the string is non-empty.
# However, converting non-standard strings to boolean may not yield expected results.  

# Exercises
# 1. Make this line of code run without errors.
print("Number of letter in your name: " + str(len(input("Enter your name: ")))) 
# str() casts the integer length to string to avoid TypeError

# 2. What will be the output of the following code? Explain why.
value = "100"
number = int(value) + 50
print(number)
# The output will be 150 because the string "100" is converted to the integer 100, 
# and then 50 is added to it.