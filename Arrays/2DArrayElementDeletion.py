import numpy as np

numpy_array = np.array([[15, 25, 17, 23], [10, 80, 55, 17], [33, 14, 47, 59]])


print(f"\nThe array before the deletion: \n{numpy_array}")

numpy_array = np.delete(numpy_array, 0, axis = 0)

print(f"\nThe array after the deletion: \n{numpy_array}")