class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we have an array of integers nums
        # return indices i and j such that 
        # nums[i] + nums[j] = target and i!=j

        # we loop over array, i 
            # we have element[i]
            # we subtract from target to get one part of sum
            # target - element[i]
            # the element we get is the element we just want to find
            # so that our summation is complete 
            # we loop over array after i as j
                # we see if j is equal to diff

        for index,element in enumerate(nums):
            diff = target - element
            print("element: ",element)
            print("diff: ",diff)
            for i,e  in enumerate(nums[index + 1:]):
                print("i", i)
                print("e", e)
                if diff == e:
                    return [index,i+index+1]
        
                    
