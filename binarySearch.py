def binarySearch(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid =(left+right)//2
        if(arr[mid]==target):
            return mid
        elif(arr[mid]>target):
            right=mid-1
        else:
            left=mid+1
    return left
print(binarySearch([2,5,8,12,16,23,38,56,72],71))