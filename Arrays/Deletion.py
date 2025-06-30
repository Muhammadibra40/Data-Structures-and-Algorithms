import array

arr_1 = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

def delete_element(arr, target):
    index = -1
    for i in range(len(arr)):
        if arr[i] == target:
            index = i
            break
    
    if index != -1:
        arr.pop(index)
        return arr
    else:
        return "Element not found"
    

def main():
    target_value = 5
    result = delete_element(arr_1, target_value)
    if isinstance(result, array.array):
        print(f"Array after deletion: {result.tolist()}")
    else:
        print(result)

    target_value_not_found = 11
    result_not_found = delete_element(arr_1, target_value_not_found)
    if isinstance(result_not_found, array.array):
        print(f"Array after deletion: {result_not_found.tolist()}")
    else:
        print(result_not_found)

if __name__ == "__main__":
    main()