def reverse_array(arr):
    x = len(arr)//2
    for i in range(x):
        arr[i],arr[-i-1] = arr[-i-1],arr[i]


arr = [10, 20, 30, 40, 50]
reverse_array(arr)
print(arr)