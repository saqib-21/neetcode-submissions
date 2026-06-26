class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res= max(nums)
        maxp=1
        minp=1 

        for n in nums:
            tmp = n * maxp
            maxp = max(maxp * n, minp * n, n)
            minp = min(tmp, minp * n, n)
            res = max(res, maxp)
        return res

