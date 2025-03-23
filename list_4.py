nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

total_sum = 0
for sublist in nested_list:
    for num in sublist:
        total_sum += num

print("\nSum of all elements in the nested list:",'\n')
