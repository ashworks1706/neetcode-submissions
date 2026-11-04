class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        stack = []
        for i in nums:
            if i in stack:
                return True
            if i not in stack:
                stack.append(i)
            
        return False