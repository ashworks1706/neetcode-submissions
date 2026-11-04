class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        has={}
        for idx,num in enumerate(nums):
            diff = target-num
            print(has)
            if diff in has:
                print(has)
                return [has[diff],idx]
            print(has)
            has[num]=idx
            print(has)