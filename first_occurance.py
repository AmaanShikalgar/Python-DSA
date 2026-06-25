def first_occurence(arr,target):
    for i in range(len(arr)):
        if(arr[i]==target):
            return i
    return -1
    
print(first_occurence(arr = [5, 8, 1, 3]
,target = 1))