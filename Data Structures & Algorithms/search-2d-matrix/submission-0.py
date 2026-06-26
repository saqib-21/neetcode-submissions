class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        print
        L,R  = 0, len(matrix) - 1 

        while L <= R: 
            MID = L+((R-L) // 2) 
            if matrix[MID][-1] < target:
                L = MID +1
            elif matrix[MID][0] > target:
                R =MID -1
            else:
                break

        if L>R:
            return False
        
        MID = L+((R-L) // 2) 
        l,r  = 0, len(matrix[MID]) - 1 

        while l <= r: 

            mid = l+((r-l) // 2) 

            if matrix[MID][mid] == target:
                return True
            elif matrix[MID][mid] > target:
                r = mid - 1 
            elif matrix[MID][mid] < target:
                l = mid + 1 

        return False