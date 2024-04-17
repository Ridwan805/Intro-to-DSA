def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        #recursive call
        mergesort(left)
        mergesort(right)

        #merging the arr
        i = 0 #keeping the track of left most element of the left array
        j = 0 #keeping the track of right most element of the right array
        k = 0 # keep tract of merged array
        while i < len(left) and j < len(right):
            
            if left[i] < right[j]:
                arr[k] = left[i]
                i+= 1
                
            else:
                arr[k] = right[j]
                j+= 1

            k+= 1

        while i < len(left):
            arr[k] = left[i]
            i+= 1
            k+= 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
        
arr = [1,5,6,3,-7,5,-6,4,2]
mergesort(arr)
print(arr)

# [-7, -6, 1, 2, 3, 4, 5, 5, 6]