def count_occurrences(arr,target):
    count = 0
    for num in arr:
        if(num==target):
            count+=1
    return count

print(count_occurrences(arr=[1,2,1,3,1],target=1))