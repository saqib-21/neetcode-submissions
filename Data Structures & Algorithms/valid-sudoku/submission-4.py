class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_check = [set() for _ in range(len(board))]
        col_check = [set() for _ in range(len(board[0]))]
        box_check = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                box = (i // 3) * 3 + (j // 3)
                if board[i][j] in col_check[j] and board[i][j] !=".":
                    return False
                if board[i][j] in row_check[i] and board[i][j] !=".":
                    return False
                if board[i][j] in box_check[box] and board[i][j] !=".":                    
                    return False           
                row_check[i].add(board[i][j])
                col_check[j].add(board[i][j])
                box_check[box].add(board[i][j])

        return True 
