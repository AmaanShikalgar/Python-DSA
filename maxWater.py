
def maxWater(height):
    left = 0
    right = len(height)-1
    max_area = 0
    
    while left<right:
        area = (right-left)*min(height[left],height[right])
        max_area = max(max_area,area)

        if(height[left]>height[right]):
            right-=1
        else:
            left+=1
    return max_area

print(maxWater([1,8,6,2,5,4,8,3,7]))