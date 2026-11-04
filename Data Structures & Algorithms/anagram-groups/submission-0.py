class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        remaining = strs.copy()  
        
        while remaining:
            current = remaining.pop(0)
            anagrams = [current]
            
            i = 0
            while i < len(remaining):
                if self.isAnagram(current, remaining[i]):
                    anagrams.append(remaining.pop(i))
                else:
                    i += 1
            
            output.append(anagrams)
        
        return output
                    
                    
    def isAnagram(self, s: str, t: str) -> bool:
        bigstr = s if len(s)>len(t) else t
        if len(s)!=len(t):
            return False
        for i in range(len(bigstr)):
            if s[i] not in t:
                return False
            t = t.replace(s[i],"",1)
        return True

