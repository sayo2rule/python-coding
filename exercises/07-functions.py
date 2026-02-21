# Functions (Built-in Functions)
print("Hello, World!")  # print() is a built-in function that outputs text to the console
num_char = len("Hello")  # len() is a built-in function that returns the length of a string
print(num_char)  # Output: 5

# Functions (User-Defined Functions)
def greet(name):
    """This function takes a name as input and prints a greeting message."""
    print(f"Hello, {name}!")  
greet("Alice")  # Output: Hello, Alice! 

def add_numbers(a, b):
    """This function takes two numbers as input and returns their sum."""
    return a + b
result = add_numbers(5, 3)  # Calling the function with arguments 5 and 3
print(result)  # Output: 8  

# Functions (Parameters and Arguments)  
def calculate_area(radius):
    """This function calculates the area of a circle given its radius."""
    import math
    area = math.pi * (radius ** 2)  # Using the formula for the area of a circle
    return area
circle_area = calculate_area(5)  # Calling the function with a radius of 5
print(circle_area)  # Output: 78.53981633974483 

# Functions (Return Values)
def square(number):
    """This function takes a number as input and returns its square."""
    return number ** 2
squared_value = square(4)  # Calling the function with the argument 4
print(squared_value)  # Output: 16

# Functions (Default Parameters)
def greet(name="Guest"):
    """This function takes a name as input and prints a greeting message. If no name is provided, it defaults to 'Guest'."""
    print(f"Hello, {name}!")
greet()  # Output: Hello, Guest!
greet("Bob")  # Output: Hello, Bob!

# Functions (Variable-Length Arguments)
def sum_numbers(*args):
    """This function takes a variable number of arguments and returns their sum."""
    total = sum(args)  # Using the built-in sum() function to calculate the total
    return total
print(sum_numbers(1, 2, 3))  # Output: 6
print(sum_numbers(4, 5))  # Output: 9

# Functions (Lambda Functions)
square = lambda x: x ** 2  # A lambda function that takes one argument and returns its square
print(square(5))  # Output: 25  

# Functions (Recursion)
def factorial(n):
    """This function calculates the factorial of a number using recursion."""
    if n == 0 or n == 1:
        return 1  # Base case: factorial of 0 or 1 is 1
    else:
        return n * factorial(n - 1)  # Recursive case: n! = n * (n-1)!
print(factorial(5))  # Output: 120

# Functions (Docstrings)
def add(a, b):
    """This function takes two numbers as input and returns their sum."""
    return a + b
print(add(10, 20))  # Output: 30
print(add.__doc__)  # Output: This function takes two numbers as input and returns their sum.   

# Functions (Scope and Lifetime)
def outer_function():
    """This is the outer function that defines a variable and an inner function."""
    outer_variable = "I am an outer variable."
    def inner_function():
        """This is the inner function that accesses the outer variable."""
        print(outer_variable)  # Accessing the outer variable from the inner function
    inner_function()  # Calling the inner function to demonstrate scope
outer_function()  # Output: I am an outer variable. 

# Functions (Higher-Order Functions)
def apply_function(func, value):
    """This function takes another function and a value, and applies the function to the value."""
    return func(value)  # Applying the passed function to the value
result = apply_function(lambda x: x ** 2, 5)  # Using a lambda function to square the value 5
print(result)  # Output: 25 

# Functions (Decorators)
def decorator_function(func):
    """This is a decorator function that wraps another function."""
    def wrapper():
        print("Before the function call.")  # Code to execute before the wrapped function
        func()  # Calling the wrapped function
        print("After the function call.")  # Code to execute after the wrapped function
    return wrapper  # Returning the wrapper function    

# Using the decorator to wrap a simple function
@decorator_function
def say_hello():
    """This function simply prints a greeting message."""
    print("Hello!")  # The actual function that will be wrapped by the decorator
say_hello()
# Output:
# Before the function call.
# Hello!
# After the function call.      

# Functions (Anonymous Functions)
# Using a lambda function to create an anonymous function that adds two numbers
add = lambda x, y: x + y  # A lambda function that takes two arguments and returns their sum
print(add(3, 4))  # Output: 7               

# Indentation and Code Blocks
def check_even_odd(number):
    """This function checks if a number is even or odd."""
    if number % 2 == 0:
        print(f"{number} is even.")  # Code block for even numbers
    else:
        print(f"{number} is odd.")  # Code block for odd numbers
check_even_odd(10)  # Output: 10 is even.
check_even_odd(7)   # Output: 7 is odd. 

# Functions (Global and Local Variables)
global_variable = "I am a global variable."  # This variable is defined in the global scope
def my_function():
    local_variable = "I am a local variable."  # This variable is defined in the local scope of the function
    print(global_variable)  # Accessing the global variable from within the function
    print(local_variable)   # Accessing the local variable from within the function
my_function()
# Output:
# I am a global variable.
# I am a local variable.    