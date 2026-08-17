class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        total= 0
        while l <= r:
            for i in range(len(piles)):
                mid =((l+r)//2)
                eaten = (piles[i] + mid - 1) // mid
                total= total +eaten
            if total<=h:
                best=mid
                total=0
                r=mid-1
            elif total>h:
                total=0
                l=mid+1
        return(best)

