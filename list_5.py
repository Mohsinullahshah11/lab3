# Week 3 => Lab 5: List Comprehensions
# Create a list of numbers from 1 to 20 containing only multiples of 3 using list comprehension.


multiples_of_3 = [num for num in range(1, 21) if num % 3 == 0]

print('\n',multiples_of_3,'\n')
