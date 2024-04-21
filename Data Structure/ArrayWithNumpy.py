#import the library numpy

import numpy as np

num = int(input("Enter the number of element in an array: "))
arr = np.zeros(num, dtype=int) # it gives a array of num length with num numbers of zeros
for i in range(num):
  arr[i] = int(input())
print(arr)