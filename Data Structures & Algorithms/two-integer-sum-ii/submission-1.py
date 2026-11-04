class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output=[]

        for index,num in enumerate(numbers):
            j=index+1
            while(j<len(numbers)):
                if(numbers[j]!=num and numbers[j] + num == target):
                    output.append(index+1)
                    output.append(j+1)
                    break
                j+=1

        return output