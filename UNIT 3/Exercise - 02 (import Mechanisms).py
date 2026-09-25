# 2. Write a program to demonstrate different import mechanisms in Python.

# 1. Import the complete module
import math

print("1. Using import module:")
print("Square root of 25 =", math.sqrt(25))


# 2. Import a specific function
from math import factorial

print("\n2. Using from module import function:")
print("Factorial of 5 =", factorial(5))


# 3. Import with an alias
import math as m

print("\n3. Using import module as alias:")
print("Value of pi =", m.pi)


# 4. Import multiple functions
from math import sqrt, pow

print("\n4. Importing multiple functions:")
print("Square root of 16 =", sqrt(16))
print("2 raised to 3 =", pow(2, 3))
