class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = [1] * length
        
        for i in range(length):
            for j in range(length):
                if i != j:
                    output[i] *= nums[j]
        return output
