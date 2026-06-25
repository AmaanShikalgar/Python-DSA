# def twosum(arr,target):
#     left = 0
#     for right in range(3,-1,-1):
#         if(arr[left]+arr[right]<target):
#             left+=1
#         if(arr[left]+arr[right]==target):
#             return [left,right]       
# print(twosum([2,7,11,15],13))

def twoSum(arr,target):
    left=0
    right = len(arr)-1
    while left<right:
        total = arr[left]+arr[right]
        if total == target:
            return[left+1,right+1]
        elif total< target:
            left+=1
        else:
            right-=1
print(twoSum([2,7,11,15],17))