class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        for i in range(len(nums)):
            for j in range(i+1, len(nums)): #do plus one since no reason to check [0]=[0]
                if nums[i] == nums[j]:
                    return True
        return False