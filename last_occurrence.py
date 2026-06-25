def last_occurrence(arr, target):
    last_index=-1

    for i in range(len(arr)):
        if arr[i]==target:
            last_index = i
    return last_index

print(last_occurrence(arr=[1,2,1,3,1],target=1))
        