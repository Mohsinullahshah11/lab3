# Week 1 => Lab 1: List Operations (Concatenation, Repetition, Membership)
# Create two lists, merge them, and check if a specific element exists in the merged list.

fruits = ['apple','bnanas','water melon']
vegetables = ['carrot', 'broccoli', 'spinach']

# merge both list
merged_list = fruits + vegetables

# check for specific element in the merged list
if 'carrot' in merged_list:
    print("\nCarrot is in the list!\n")
else:
    print("\nCarrot is not in the list.\n")
