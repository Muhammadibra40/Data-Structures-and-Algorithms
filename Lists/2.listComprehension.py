# List Comprehension is only in python.
# can be used aslo with Range, String and Tuple

prev_list = [1, 2, 3]
new_list = []

for val in prev_list:
    new_list.append(val * 2)

print(new_list)


new_list_2 = [i * 2 for i in prev_list]
print(new_list_2)


word = "python"
new_list = [char for char in word]
print(new_list)


# Confitional List Comprehantion
num_list = [1, 2, 5, -1, 6, -11, 25, 0]
neg_num = [num*num for num in num_list if num < 0]
print(neg_num)

neg_num_with_zeros = [num if num < 0 else "neg_num" for num in num_list]
print(neg_num_with_zeros)

def is_consonant(letter):
    vowels = "aeiou"
    return letter.isalpha() and letter.lower() not in vowels

print(is_consonant("a"))
print(is_consonant("t"))


sen = "My name is Muhammad"
consonant_letters = [letter for letter in sen if is_consonant(letter)]

print(consonant_letters)
