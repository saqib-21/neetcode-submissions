class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #first we need to sort the list in order 

        nums.sort()

        sum_results=[]

        for i in range(len(nums)):
            print(i)
            if nums[i] > 0:
                break
            if i > 0 and nums[i-1] == nums[i]:
                continue 
            a = nums[i]
            print(a)
            bc=self.find_bc(nums, i+1, -a)

            for pair in bc:
                sum_results.append([a, pair[0], pair[1]])
        return sum_results

    def find_bc(self, nums: List[int], start: int, target: int)-> List[List[int]]:
        b = start 
        c = len(nums)-1

        pair_results = []
    
        while b<c:
            s = nums[b] + nums[c]
            print(nums[b] + nums[c])
            if s == target:
                pair_results.append([nums[b], nums[c]])
                b+=1
                while b<c and nums[b] == nums[b-1]:
                    b+=1
            elif s < target:
                b+=1
            else:
                c-=1
        return pair_results

 

