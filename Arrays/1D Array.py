import array
import numpy as np

# This code snippet demonstrates how to create a 1D array using the array module in Python and print its elements.
arr_1 = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Travere of a 1D array
for i in arr_1:
    print(i, end=' ')

print("\n\n")
# Arrays only accepts the same data types but list accepts different data types.

# nums in the array will be treated as chars.
arr = np.array([1, 2, 3, 4, 5, 'a'])
list = [1, 2, 3, 4, 'a']


print(arr)
print(list)