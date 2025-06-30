import array

print("\n1. Creation of an array.")
arr_1 = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print("\n2. Array Traversal.")
for i in arr_1:
    print(i, end=' ')

print("\n\n3. Element Access in an array using index.")
print(arr_1[0])

print("\n\n4. Element Appending in an array using append() method.")
arr_1.append(11)
print(arr_1)

print("\n\n5. Element Insertion in an array using insert(index, value) method.")
arr_1.insert(2, 55)
print(arr_1)


print("\n\n6. Array Extension by another array using the extend() method.")

arr_2 = array.array('i', [100, 202])
arr_1.extend(arr_2)
print(arr_1)


print("\n\n7. Items Addition from a list using the fromlist() method.")

tempList = [555, 666]
arr_1.fromlist(tempList)
print(arr_1)

# The remove() method only deletes the first occurance of the targeted value if it's duplicated.
print("\n\n8. Element Deletion from a list using the remove() method.")

arr_1.remove(555)
print(arr_1)


print("\n\n9. Last element Deletion from a list using the pop() method.")

arr_1.pop()
print(arr_1)


print("\n\n10. Geting the element index using the index() method.")
print(arr_1.index(1))



print("\n\n11. Reverse of the array using the revrese() method.")
arr_1.reverse()

print(arr_1)


print("\n\n12. Buffer Information of the array using the buffer_info() method.")
print(arr_1.buffer_info())


print("\n\n13. Counting the no. of occurances of an element in the array using the count() method.")
print(arr_1.count(10))


print("\n\n14. Converting an array to a list using the tolist() method.")

tempList = arr_1.tolist()
print(arr_1)
print(tempList)


print("\n\n15. Slicing an array.")


print(arr_1[1:5])
print(arr_1[:5])
print(arr_1[1:])
print(arr_1[-5:-1])
print(arr_1[:])