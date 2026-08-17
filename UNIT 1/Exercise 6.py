#6) Write a program to illustrate the use of tuples and sets with basic operations. 

print("----- TUPLE -----")
numbers = (10, 20, 30, 40, 50)
print("Tuple:", numbers)

# Indexing
print("First element:", numbers[0])
print("First three elements:", numbers[:3])
print("Length of tuple:", len(numbers))
print("Count of 20:", numbers.count(20))
print("Index of 40:", numbers.index(40))

print("\n----- SET -----")
# Sets
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print("Set 1:", set1)
print("Set 2:", set2)

set1.add(50)
print("After adding 50:", set1)

set1.remove(10)
print("After removing 10:", set1)

print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference:", set1.difference(set2))