class Solution:
    def pair(self,b,target, nums):
            l = b
            r=len(nums)-1
            pairs = []

            while l<r:
                total = nums[l]+nums[r]
                if total ==target:
                    found = [nums[l],nums[r]]
                    pairs.append(found)
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                elif total > target:
                    r-=1         
                elif total < target:
                    l+=1
            return pairs


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        triplet = []
        nums = sorted(nums)

        for i in range(n):
            #if a is postive not possible to add sum
            if nums[i] > 0:
                break
            if i > 0 and nums[i]==nums[i-1]:
                 continue
            else:
                two_nums=self.pair(i+1,-nums[i],nums)
                for p in two_nums:
                    triplet.append([nums[i]] + p)
        return triplet

    

