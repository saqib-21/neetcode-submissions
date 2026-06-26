class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0


        #while index of right point is in the list 
        #max r can be (index 3) max size of list (4) so if (1,4,2,5) r[3] = 5
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1
        return maxProfit