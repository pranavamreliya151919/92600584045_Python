#7) Write a program to create a dictionary and demonstrate dictionary methods and iteration. 

student = {
    "name": "Pranav",
    "age": 20,
    "course": "Python"
}

# Access value
print(student["name"])

# Dictionary methods
print(student.keys())
print(student.values())
print(student.items())

# Add value
student["city"] = "Gujarat"

# Iteration
for key, value in student.items():
    print(key, ":", value)
