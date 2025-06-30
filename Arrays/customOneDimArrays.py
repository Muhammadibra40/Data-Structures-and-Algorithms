class CustomOneDArray:
    def __init__(self, data_type, capacity):
        self.data_type = data_type
        self.capacity = capacity
        self.length = 0
        self.data = [None] * self.capacity

    @classmethod
    def createArray(cls, data_type, elements_list):
        array_obj = cls(data_type, len(elements_list) * 2)  # Create with some extra space
        for element in elements_list:
            if not isinstance(element, data_type):
                raise TypeError(f"All elements must be of type {data_type.__name__}")
            array_obj.data[array_obj.length] = element
            array_obj.length += 1
        return array_obj

    
    def insert(self, value):
        if self.length < self.capacity:
            self.data[self.length] = value
            self.length += 1
        else:
            print("Array is full. Cannot insert new element.")

    def delete(self, value):
        if self.length != 0:
            for i in range(self.length):
                if self.data[i] == value:
                    for j in range(i, self.length - 1):
                        self.data[i] = self.data[i+1]
                    self.data[self.length] = None
                    self.length -= 1
        else:
            print("The array is alreay empty.")

    def display(self):
        if self.length != 0:
            print("\n")
            for i in range(self.length):
                print(f"{self.data[i]}", end=' ')
        else:
            print("Array is empty. Cannot show any element.")

    def getElement(self, index):
        if index < 0 or index >= self.length:
            print("Invalid index.")
            return
        else:
            return self.data[index]

arr = CustomOneDArray(str, 5)

arr.insert(10)
arr.insert(20)
arr.insert(30)


# print(arr)
arr.display()  # Output: [10, 20, 30]


arr.delete(10)
arr.display()  # Output: [10, 30]

arr_1 = CustomOneDArray.createArray(int, [10, 20, 30, 40])
arr_1.display()
arr_2 = CustomOneDArray.createArray(int, [10, "20", 30, 40])

