class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lookup = {}
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in lookup:
                return [lookup[complement] + 1, i + 1]
            lookup[num] = i
