import numpy as np

def selectionSort(arr,size):

    for i in range(size-1):
        
        min = i

        for j in range(i+1,size):
            if arr[j] < arr[min]:
                min = j 
        
        arr[i],arr[min] = arr[min],arr[i]

n = int(input("Number of Data: "))
arr = np.zeros(n, dtype = int)
for i in range(n):
  arr[i] = int(input("Enter the element: "))

print("The array is ",arr)

selectionSort(arr,n)
print("After sorting: ", arr)
