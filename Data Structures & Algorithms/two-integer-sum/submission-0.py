class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            #checks if this is the second value is the remaing value needed to get to target 
            #[3,4,5] and t=7 currently in the hashmap is 3:0 so 4 would make it equal the t since the diff 7-4 in the prevmap
            if diff in prevMap:
                return [prevMap[diff], i]
            #put into hashmap
            prevMap[n] = i