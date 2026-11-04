class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # check if unordered string s1 is present in s2 consecutively 
        
        # s1 = sorted(s1)
        # s2 = sorted(s2)
        # print(s2)
        
        # print(s1_cop)
        for i in range(len(s2) - len(s1) + 1):
            s1_cop = s1
            for j in range(i, i + len(s1)):
                if s2[j] in s1_cop:
                    s1_cop = s1_cop.replace(s2[j], "", 1)
                    if len(s1_cop) == 0:
                        return True
                else:
                    break
        
        # print("s1_cop : ", s1_cop)
        

        return False