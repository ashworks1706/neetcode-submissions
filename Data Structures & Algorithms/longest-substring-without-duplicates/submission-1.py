class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # longest substring without repeating chars


        # we start from left and right
        # we keep shrinking until substring does not contain duplicates
        
        maxlen = 0
        hashset = set()

        l =0

        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l+=1
            hashset.add(s[r])
            maxlen = max(maxlen, r - l + 1)
        return maxlen