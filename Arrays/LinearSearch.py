import array

arr_1 = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

def main():
    target_value = 5
    result = linear_search(arr_1, target_value)
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("The number is not present in the array")

    target_value_not_found = 11
    result_not_found = linear_search(arr_1, target_value_not_found)
    if result_not_found != -1:
        print(f"Element found at index: {result_not_found}")
    else:
        print("The number is not present in the array")

if __name__ == "__main__":
    main()
