def first_and_last(arr, target):
    first_index =-1
    last_index=-1 
    for i in range(len(arr)):
        if(arr[i]==target):
            if first_index == -1:
                first_index = i
            last_index=i
    return first_index,last_index

print(first_and_last(arr=[1,2,1,3,1],target=1))