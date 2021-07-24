def insertion(arr):
    for i in range(1,len(arr)-1):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
    return arr

a = [5,2,4,6,1,3]
print(insertion(a)) # [1, 2, 4, 5, 6, 3]