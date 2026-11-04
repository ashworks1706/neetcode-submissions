class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if two strings have exact same chars but order is diff
        
        # we can use hash set here since we're checking O(1)

        # sort strings

        s = "".join(sorted(s))
        t = "".join(sorted(t))

        if t == s:
            return True

        return False