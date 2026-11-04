class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(open_count, close_count, current_string):
            if len(current_string) == 2 * n:
                result.append(current_string)
                return
            
            if open_count < n:
                backtrack(open_count + 1, close_count, current_string + "(")
            
            if close_count < open_count:
                backtrack(open_count, close_count + 1, current_string + ")")

        result = []
        backtrack(0, 0, "")
        return result
