class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            #if our number is bigger then we want to move r left since it will lead to smaller r thus smaller sum 
            if curSum > target:
                r -= 1

            #if our number is smaller (<target) then we want to move l right since it will lead to bigger l thus bigger sum 
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []