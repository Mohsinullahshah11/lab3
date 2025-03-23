# Week 2 => Lab 3: Common List Methods
# Create a list and perform append, extend, insert, remove, pop, sort, and reverse operations.


# Create a list
fruits = ['apple', 'banana', 'cherry']
print("Initial List:", fruits)

# 1. Append - Adds a single element at the end
fruits.append('orange')
print("After append('orange'):", fruits)

# 2. Extend - Adds multiple elements at the end
fruits.extend(['mango', 'grapes'])
print("After extend(['mango', 'grapes']):", fruits)

# 3. Insert - Inserts an element at a specific position
fruits.insert(2, 'kiwi')  # Insert 'kiwi' at index 2
print("After insert(2, 'kiwi'):", fruits)

# 4. Remove - Removes the first occurrence of the specified element
fruits.remove('banana')
print("After remove('banana'):", fruits)

# 5. Pop - Removes element by index (last element by default)
popped_fruit = fruits.pop()  # Removes 'grapes'
print("After pop():", fruits)
print("Popped element:", popped_fruit)

# 6. Sort - Sorts the list in ascending order
fruits.sort()
print("After sort():", fruits)

# 7. Reverse - Reverses the list
fruits.reverse()
print("After reverse():", fruits)
