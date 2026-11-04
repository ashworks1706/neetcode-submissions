class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # array of days
        # days[i] is the temperature of the day 
        # function returns array of results -> days
        # results[i] is no. of days between days[results[i]] and next 
        # warmer day(greater number)
        #  if theres no warmer day after results[i] we will return 0

        n = len(temperatures)
        result = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            stack.append(i)

        return result
