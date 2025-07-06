# Lists can have different types of elements.
# Lists can have nested lists


fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1             # Reference copy (points to same list)
fruit_list3 = fruit_list1[:]          # Shallow copy (independent list)

# O/P
# fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
# fruit_list2 = ['Apple', 'Berry', 'Cherry', 'Papaya']   # same as fruit_list1
# fruit_list3 = ['Apple', 'Berry', 'Cherry', 'Papaya']   # separate copy

fruit_list2[0] = 'Guava'   # modifies fruit_list1 as well, since fruit_list2 is just a reference
fruit_list3[1] = 'Kiwi'    # modifies only fruit_list3


# O/P
# fruit_list1 = ['Guava', 'Berry', 'Cherry', 'Papaya']
# fruit_list2 = ['Guava', 'Berry', 'Cherry', 'Papaya']   # same as fruit_list1
# fruit_list3 = ['Apple', 'Kiwi', 'Cherry', 'Papaya']



list1 = ["Milk", "coffee", "banana"]

list1[:2] = ["Jam", "oil"]

# list1[3] = "berries" Out of index error and doesn't add this element to the list.

# Insertion of an element in a specific index and the elements after will be shifted O(n) time complexity.
list1.insert(1, 55)
print(list1)

# Insertion of an element at the end of the list.
list1.append(66)
list1.append([222])
print(list1)

# Extension of a liat by adding another list to it. O(n) time & space complexity as it iterates through all the elements of the new list and add them.
list2 = [5, 6, 7, 8]
list1.extend(list2)
print(list1)


# Deletion methods in Lists.
# 1. pop()
# 2. remove()
# 3. del

# time complexity without using an index = O(1)/ time complexity of a specified index, aslo if it was the first element = O(n)
# space complexity = O(1)
deleted_element = list1.pop(1)

# The last element.
deleted_element = list1.pop()

print(list1)

# time complexity = O(n)
# space complexity = O(1)
del list1[:2]
print(list1)

# Deletion of an element without knowing its index.
# time complexity = O(n)
# space complexity = O(1)
list1.remove(66)
print(list1)

# --------------------------------------------------------------------------------------------- #
# Searching in Lists.
# --------------------------------------------------------------------------------------------- #

# 1. in operator: performs a linear search under the hood.
# Time complexity = O(1)
new_list = [1, 2, 3, 4, "Mango"]

print(1 in new_list)

# 2. Linear Search

# --------------------------------------------------------------------------------------------- #
# Operators/ Functions in Lists.
# --------------------------------------------------------------------------------------------- #
# + Operator: concatination of lists.

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b

print(c)

# * Operator: Repeatation of elements.
a = a * 2
print(a)

# a = a * b
# print(a)

# max()/ min() funtion: returns the max/ min value in a list.

max_val = max(a)
print(max_val)

# TypeError: '>' not supported between instances of 'int' and 'str'.
# max only used in a list with the same datatypes.
# max_val = max(list1)
# print(max_val)

str_list = ["apple", "cake", "orange"]
print(max(str_list))

# sum()/ len()


# num_list = []
# while(True):
#     in_val = input("Enter a number: ")
#     if in_val == 'done': break
#     num_list.append(int(in_val))
# print('Average: ', sum(num_list)/len(num_list))


# list() function

str = "spam"
str_list = list(str)
print(str_list)

# split() mehtod

str_ex = "spam-spam-spam"
list_ex = str_ex.split("-")
print(list_ex)

# join() function
list_ex = "-".join(list_ex)
print(list_ex)

# sort() method "in-place" vs. sorted() function "out-of-place"

