class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        bigstr = s if len(s)>len(t) else t
        if len(s)!=len(t):
            return False
        for i in range(len(bigstr)):
            if s[i] not in t:
                return False
            t = t.replace(s[i],"",1)
        return True