class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # In this case, all indices would be stored in the stack.
        # The algorithm uses a stack to keep track of the indices of the temperatures.
        # It iterates through the temperatures list, and for each temperature,
        # it checks if the current temperature is greater than the temperature at the index stored at the top of the stack.
        # If it is, it means that the current temperature is the next warmer temperature for the index stored at the top of the stack.
        # The algorithm continues to pop indices from the stack until it finds a temperature that is greater than the current temperature.
        # The difference between the current index and the popped index gives the number of days until a warmer temperature.
        # If the stack is empty, it means that there is no warmer temperature in the future for that index,
        # and the result for that index remains 0.
        # The algorithm returns the result list containing the number of days until a warmer temperature for each day.
        n = len(temperatures)
        result = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                result[j] = i - j
            stack.append(i)

        return result