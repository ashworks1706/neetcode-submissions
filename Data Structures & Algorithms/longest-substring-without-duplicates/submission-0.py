class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # longest substring without repeating chars


        # we start from left and right
        # we keep shrinking until substring does not contain duplicates
        
        max_len = 0
        l = 0
        chars = set()
        
        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            max_len = max(max_len, r - l + 1)
            
        return max_len