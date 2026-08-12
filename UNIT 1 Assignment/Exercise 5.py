# Creating a list
numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

# 1. Indexing
print("\n--- Indexing ---")
print("First element:", numbers[0])
print("Third element:", numbers[2])
print("Last element:", numbers[-1])

# 2. Slicing
print("\n--- Slicing ---")
print("First three elements:", numbers[:3])
print("Elements from index 2:", numbers[2:])
print("Middle elements:", numbers[1:4])
print("Reverse list:", numbers[::-1])

# 3. Manipulating the list
print("\n--- List Manipulation ---")
numbers.append(60)
print("After append:", numbers)

numbers.insert(1, 15)
print("After insert:", numbers)

numbers.remove(30)
print("After remove:", numbers)

# 4. List Comprehension
print("\n--- List Comprehension ---")
squares = [x * x for x in numbers]
print("Square of each element:", squares)

even = [x for x in numbers if x % 2 == 0]
print("Even numbers:", even)
