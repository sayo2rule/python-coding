# Number manipulation
number = 7.89
# Rounding
rounded_number = round(number)
print(rounded_number)  # 8
# Absolute value
absolute_number = abs(-number)
print(absolute_number)  # 7.89
# Type casting
int_number = int(number)
print(int_number)  # 7      

score = 0
# User score a point
score += 1  # score = score + 1
print(score)  # 1
# User score 5 more points
score += 5  # score = score + 5
print(score)  # 6
# User loses 2 points
score -= 2  # score = score - 2
print(score)  # 4
# User's score is doubled
score *= 2  # score = score * 2
print(score)  # 8
# User's score is halved
score /= 2  # score = score / 2
print(score)  # 4.0
# User's score is floored
score //= 2  # score = score // 2
print(score)  # 2.0
# User's score modulus 2
score %= 2  # score = score % 2
print(score)  # 0.0
# User's score raised to the power of 3
score **= 3  # score = score ** 3
print(score)  # 0.0 


# Mathematical operations with mixed data types
# Addition
result1 = 10 + 5.5  # int + float
print(result1)  # 15.5  

result2 = "Hello, " + "World!"  # str + str
print(result2)  # Hello, World!
# Uncommenting the following line will raise a TypeError
# result3 = "Age: " + 30  # str + int

# Subtraction
result4 = 20.0 - 5  # float - int
print(result4)  # 15.0
# Uncommenting the following line will raise a TypeError
# result5 = "100" - "50"  # str - str

# Multiplication
result6 = 4 * 2.5  # int * float
print(result6)  # 10.0

result7 = "Ha" * 3  # str * int
print(result7)  # HaHaHa
# Uncommenting the following line will raise a TypeError
# result8 = "Hello" * 2.5  # str * float

# Division
result9 = 15 / 2  # int / int
print(result9)  # 7.5
result10 = 7.5 / 2.5  # float / float
print(result10)  # 3.0
# Uncommenting the following line will raise a TypeError
# result11 = "100" / "2"  # str / str

# Floor Division
result12 = 15 // 2  # int // int
print(result12)  # 7
result13 = 7.5 // 2.5  # float // float
print(result13)  # 3.0
# Uncommenting the following line will raise a TypeError
# result14 = "100" // "2"  # str // str

# Modulus
result15 = 10 % 3  # int % int
print(result15)  # 1
result16 = 7.5 % 2.5  # float % float
print(result16)  # 0.0
# Uncommenting the following line will raise a TypeError
# result17 = "10" % "3"  # str % str

# Exponentiation
result18 = 2 ** 3  # int ** int
print(result18)  # 8
result19 = 9.0 ** 0.5  # float ** float
print(result19)  # 3.0
# Uncommenting the following line will raise a TypeError
# result20 = "2" ** "3"  # str ** str   


# PEMDAS/BODMAS order of operations
result = 3 + 5 * 2 - (4 / 2) ** 2
# Step 1: Parentheses
# (4 / 2) = 2.0
# Step 2: Exponents
# 2.0 ** 2 = 4.0
# Step 3: Multiplication
# 5 * 2 = 10
# Step 4: Addition and Subtraction from left to right
# 3 + 10 - 4.0 = 9.0
print(result)  # 9.0

# Exercise
# hat is the data type of the result of the variable a in the following line of code:
a = int("5") / int(2.7)
print(type(a))  # <class 'float'>