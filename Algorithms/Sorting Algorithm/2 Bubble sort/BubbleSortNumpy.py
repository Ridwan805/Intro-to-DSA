import numpy as np
def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

n = int(input("Number of Data: "))
arr = np.zeros(n, dtype = int)
for i in range(n):
  arr[i] = int(input("Enter the element: "))

bubbleSort(arr)

print("The array is ",arr)
