#Data Types

#String
print("Hello")

#Integer
print(123)

#Float
print(3.14159)

#Boolean
print(True)
print(False)

#Type Errors
num_char = len(input("What is your name?"))

#Type Checking
print(type(num_char))

#Type Conversion
#str()
#int()
#float()
#bool()
      
new_num_char =str(num_char)
print("Your name has " + new_num_char + " characters.")
# Maths Operations
#3 + 5
#7 - 4
#3 * 2
#6 / 3
#2 ** 3

# PEMDASLR (Parentheses, Exponents, Multiply & Divide, Add & Subtract, Left to Right)
# ()
# **
# * /
# + -

print(3 * (3 + 3) / 3 - 3)

#Rounding Numbers
#round up to 2 decimal place
print(round(4.6666666666,2))

#Floor division means the ans will be in int
print(9 // 4)
print(9/4)

#Shorthand Operators
# a += 2  short for a = a + 2
# -=
# *=
# /=


#f-Strings
score = 0
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")