from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return top k frequent elements
        
        # we can use hash set here to track the freq of element

        # tracked = hashset

        count = Counter(nums)
        
        # we make an empty list of items that are in the list

        buckets = [[] for _ in range(len(nums)+1)]

        for num, freq in count.items():
            buckets[freq].append(num)

        print(buckets)

        results =[]

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                results.append(num)
                if len(results)==k:
                    return results

        return k
