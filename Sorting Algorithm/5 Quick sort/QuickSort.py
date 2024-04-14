def quicksort(arr,low,high):
    if low < high:
        pivot = partition(arr,low,high)
        quicksort(arr,low,pivot-1)
        quicksort(arr,pivot+1,high)
    return arr


def partition(arr,low,high):
    pivot = arr[high]
    x = low - 1 
    for i in range(low,high):
        if arr[i] <= pivot:
            x+= 1
            arr[x],arr[i] = arr[i],arr[x]
    arr[x+1],arr[high] = arr[high],arr[x+1]
    return x+1

arr = [12, 11, 13, 5, 6]
l = len(arr)-1 
quicksort(arr,0,l)

print(arr)