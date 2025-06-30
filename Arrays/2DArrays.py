import numpy as np

twoDArray = np.array([[10, 15, 17], [20, 25, 28], [66, 44, 88]])

tempArray = [[15, 16, 17]]

# Insrtion of a row in a specific position.
twoDArray = np.insert(twoDArray, 1, tempArray, axis=0)

print(twoDArray, "\n\n 1. Insertion of a row in a specific position.\n")

# Insrtion of a column in a specific position.
twoDArray = np.insert(twoDArray, 1, [100, 200, 300, 400], axis=1)
print(twoDArray, "\n 2. Insertion of a column in a specific position.\n")


# Deletion of a row in a specific position.
twoDArray = np.delete(twoDArray, 1, axis=0)
print(twoDArray, "\n 3. Deletion of a row in a specific position.\n")

# Deletion of a column in a specific position.
twoDArray = np.delete(twoDArray, 1, axis=1)
print(twoDArray, "\n 4. Deletion of a column in a specific position.\n")


# Accessing a specific element in the 2D array.
print(twoDArray[0, 1], "\n 5. Accessing a specific element in the 2D array.\n")


def accessElement(array, rowIndex, colIndedx):
    if rowIndex < array.shape[0] and colIndedx < array.shape[1]:
        return array[rowIndex, colIndedx]
    else:
        return "Index out of bounds"
    
# Accessing a specific element using a function.
print(accessElement(twoDArray, 0, 1), "\n 6. Accessing a specific element using a function.\n")
    

def traverseTDArray(twoDArray):
    for i in range(twoDArray.shape[0]):
        print(f"\nRow No. {i+1}")
        for j in range(twoDArray.shape[1]):
            print(twoDArray[i][j], end=' ')


traverseTDArray(twoDArray)


def searchTDArray(twoDArray, val):
    for i in range(twoDArray.shape[0]):
        for j in range(twoDArray.shape[1]):
            if twoDArray[i][j] == val:
                return f'\n\nThe value {val} was found at index: ' +str(i)+", "+str(j)
    return f"\n\nThe value {val} was not found"
        
def main():         
    found_val = 15
    not_found_val = 444

    print(searchTDArray(twoDArray, found_val))
    print(searchTDArray(twoDArray, not_found_val))

if __name__ == "__main__":
    main()

            
