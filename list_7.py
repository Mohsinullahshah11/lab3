# Week 4: => Lab 7: List Performance & Optimization
# Use deque to implement a queue where elements are added and removed efficiently. 

# Append to the right    d.append(5)                Adds 5 to the right end
# Append to the left     d.appendleft(0)            Adds 0 to the left end
# Pop from the right     d.pop()                    Removes and returns the rightmost element
# Pop from the left      d.popleft()                Removes and returns the leftmost element
# Extend right           d.extend([5, 6])           Adds multiple elements to the right
# Extend left            d.extendleft([-1, -2])     Adds multiple elements to the left (in reverse order)
# Rotate                 d.rotate(1)                Rotates right by 1 step
# Rotate left            d.rotate(-1)               Rotates left by 1 step

from collections import deque

list_1 = deque([1,2,3,4,5,6])

list_1.append(23) # [1, 2, 3, 4, 5, 6, 23]
list_1.appendleft(3)  # [3, 1, 2, 3, 4, 5, 6, 23]

print(list_1.pop()) # return 23(last element) and also remove it from the list => [3, 1, 2, 3, 4, 5, 6]
print(list_1.popleft()) # return 3(First Element) and also remove it from the list => [1, 2, 3, 4, 5, 6]


print(list_1)