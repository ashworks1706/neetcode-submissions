class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for d_ar in strs:
            d_arrstring = ''.join(sorted(d_ar))
            res[d_arrstring].append(d_ar)
        
        return list(res.values())
