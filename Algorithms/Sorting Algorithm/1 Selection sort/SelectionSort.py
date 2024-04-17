def selectionSort(arr,size):

    for i in range(size-1):
        
        min = i

        for j in range(i+1,size):
            if arr[j] < arr[min]:
                min = j 
        
        arr[i],arr[min] = arr[min],arr[i]

x = [1,6,3,5,-84,-6,-7,-3,-2,0]

selectionSort(x,len(x))

print(x)
