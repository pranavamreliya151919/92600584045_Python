#4) Write a program to demonstrate string operations including slicing formatting and built-in string functions.

x="Marwadi University"
#Slicing
print("Your String Is :",x)
print("First 2 Character :",x[:2])
print("Last 2 Character :",x[-2:])
print("Reverse :",x[::-1])
print("0 To 5 Index Number :",x[0:5])

#String Function
print("Uppercase:", x.upper())
print("Lowercase:", x.lower())
print("Capitalized:", x.capitalize())
print("Title Case:", x.title())
print("Length:", len(x))
print("Replace:", x.replace("Marwadi", "world"))
print("Count of 'a':", x.count("a"))
print("Position of 'University':", x.find("University"))

word = x.split()
print("After split:", word)
print("First word:", word[0])
print("Second word:", word[1])

y = "   Marwadi University   "
print("Before strip:", y)
print("After strip:", y.strip())

words = ["Marwadi", "University"]
result = " ".join(words)
print(result)

print("Is alphabetic:", x.isalpha())
print("Is digit:", x.isdigit())
print("Starts with 'Marwadi':", x.startswith("Marwadi"))
print("Ends with 'University':", x.endswith("University"))

#String Formatting 
student="Pranav"
age=20
print(f"My Name is {student} and my age is {age}.")
print("My name is {} and my age is {}.".format(student, age))


