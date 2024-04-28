import numpy as np

def insertionSort(arr):

    for i in range(1,len(arr)):
        temp = arr[i]
        
        j = i - 1 
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp

num = int(input("Enter the number of elements: "))
arr = np.zeros(num, dtype = int)
for i in range(num):
  arr[i] = int(input("Enter the element: "))

insertionSort(arr)

print(arr)
