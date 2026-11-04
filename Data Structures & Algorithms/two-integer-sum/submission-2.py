class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx,i in enumerate(nums):
            print(f"idx : {idx}")
            for idex,j in enumerate(nums[idx+1:], start=idx+1):
                print(f"idex : {idex}")
                if i+j == target:
                    return [idx,idex]
        return []
