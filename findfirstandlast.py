def searchRange(nums,target):
    left=0
    right=len(nums)-1
    while left<right:
        mid=(left+right)//2
        if(nums[mid]>=target):
            right=mid
        else:
            left=mid+1
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid
        return [nums[left],nums[left+1]]
print(searchRange([5,7,7,8,8,10],7))