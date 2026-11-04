class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()  
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue  
            temp = nums[i+1:] 
            j = 0
            while j < len(temp):
                k = j + 1
                while k < len(temp):
                    if temp[j] + temp[k] + num == 0:
                        triplet = [num, temp[j], temp[k]]
                        triplet.sort()  
                        if triplet not in output:
                            output.append(triplet)
                        break
                    k += 1
                j += 1
        return output
