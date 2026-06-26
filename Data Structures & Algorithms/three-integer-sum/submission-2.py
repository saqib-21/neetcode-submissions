class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            a = nums[i]

            #first we make a our sum and try to have b and c eqaul to a
            #check if a is negative since after sorting the smallest a value should be negatvie and if it is psotive then b and c cant be equal to -(+a) 
            if a > 0:
                break

            #check if the number after a is not a duplicat 
            if i > 0 and a == nums[i - 1]:
                continue

                
            #now find b and c which cancels out a 
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    #if new b is the same as old one move one more again.
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res