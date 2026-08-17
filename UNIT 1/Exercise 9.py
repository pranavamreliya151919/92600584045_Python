#9) Write a program to define and use user-defined functions with different types of arguments. 

# No argument
def hello():
    print("Hello")

hello()

# Positional arguments
def add(a, b):
    print(a + b)

add(15, 35)

# Default argument
def greet(name="Pranav Amreliya"):
    print("Hello", name)

greet()
greet("Abhijeet")
