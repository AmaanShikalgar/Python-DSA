def minEatingSpeed(piles , h):
        left=1
        right=max(piles)

        def canFinish(mid):
            hours = 0
            for pile in piles:
                hours += (pile+mid-1)//mid
            return hours <=h

        while left<right:
            mid=(left+right)//2
            
            if canFinish(mid):
                right = mid
            else:
                left=mid+1
        return left