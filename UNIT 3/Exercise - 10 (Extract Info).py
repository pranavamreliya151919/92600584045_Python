#Write a program to extract specific information from a text file using regular expressions.

import re

# Create and write data into file
with open("data.txt", "w") as file:
    file.write("Name: Pranav Amreliya\n")
    file.write("Email: pranav.amreliya151919@marwadiuniversity.ac.in\n")
    file.write("Phone: 9913156214\n")

# Read file
with open("data.txt", "r") as file:
    text = file.read()

# Extract information
emails = re.findall(r'\S+@\S+\.\S+', text)
phones = re.findall(r'\d{10}', text)

print("Email:", emails)
print("Phone:", phones)
