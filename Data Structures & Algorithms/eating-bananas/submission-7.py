class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l <= r:
            mid =((l+r)//2)
            total= 0
            for p in (piles):
            
                #time_eaten = (piles[i] + mid - 1) // mid
                total+= math.ceil(p/mid)
            if total<=h:
                best=mid
                total=0
                r=mid-1
            elif total>h:
                total=0
                l=mid+1
        return(best)
