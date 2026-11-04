class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # checking the rows
        for row in board:
            seen = set()
            for element in row:
                if element != '.' and element in seen:
                    return False
                seen.add(element)
        print("Row Check Passed!")

        # checking the columns
        for col in range(len(board)):
            seen = set()
            for row in range(len(board)):
                element = board[row][col]
                if element != '.' and element in seen:
                    return False
                seen.add(element)
        print("Column Check Passed!")

        # checking the quarters
        for box_row in range(0, len(board), 3):
            for box_col in range(0, len(board), 3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        element = board[box_row + i][box_col + j]
                        if element != '.' and element in seen:
                            return False
                        seen.add(element)
        print("Quarters Check Passed!")
        return True
