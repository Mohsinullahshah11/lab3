# Week 3 => Lab 6: Working with Nested Lists
# Write a program to find the sum of all elements in a nested list.


# Week 2 => Lab 4: Iterating Over Lists
# Write a program to print each element of a list with its index using enumerate.

nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

total_sum = 0
for sublist in nested_list:
    for num in sublist:
        total_sum += num

print("\nSum of all elements in the nested list:",'\n')
