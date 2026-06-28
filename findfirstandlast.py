def searchRange(nums,target):
    def findFirst():
        left=0
        right=len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid] >= target:
                right=mid
            else:
                left=mid+1
        if len(nums)==0:
            return -1
        if left < len(nums) and nums[left]==target:
            return left
        return -1
    def findLast():
        left=0
        right=len(nums)-1
        while left<right:
            mid=(left+right+1)//2
            if nums[mid]<=target:
                left=mid
            else:
                right=mid-1
        if len(nums)==0:
            return -1
        if nums[left] == target:
            return left
        return -1
    return[findFirst(),findLast()]
print(searchRange([5,7,7,8,8,10],8))