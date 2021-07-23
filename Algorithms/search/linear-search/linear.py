def linearSearch(arr,searchElement):
    for i in range(0,len(arr)):
        if(arr[i] == searchElement):
            return i
    return -1

arr = [1,4,5,6,9]

print(linearSearch(arr,6)) # 3
print(linearSearch(arr,99)) # -1
