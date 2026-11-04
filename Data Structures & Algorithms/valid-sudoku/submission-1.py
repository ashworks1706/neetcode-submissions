class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in range(9):
            seen = set()
            for col in range(9):
                cell = board[row][col]
                if cell != "." and cell in seen:
                    return False
                elif cell != ".":
                    seen.add(cell)
        
        # Check columns
        for col in range(9):
            seen = set()
            for row in range(9):
                cell = board[row][col]
                if cell != "." and cell in seen:
                    return False
                elif cell != ".":
                    seen.add(cell)
        
        # Check 3x3 sub-boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen = set()
                for row in range(box_row, box_row + 3):
                    for col in range(box_col, box_col + 3):
                        cell = board[row][col]
                        if cell != "." and cell in seen:
                            return False
                        elif cell != ".":
                            seen.add(cell)
        
        # If all checks pass, the board is valid
        return True
