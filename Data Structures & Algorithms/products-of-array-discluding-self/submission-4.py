import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # at index i, calculate product of all integers in array except at i
        # add product to that position in array 

        # O(n) time required

        # we can loop over array i 
            # get integers except that i by nums[:i] + nums[i:]
            # sum those intgers add to list

        res = []
        for index, num in enumerate(nums):
            excpt = nums[:index] + nums[index+1:]
            prod = math.prod(excpt)
            res.append(prod)
        
        return res
