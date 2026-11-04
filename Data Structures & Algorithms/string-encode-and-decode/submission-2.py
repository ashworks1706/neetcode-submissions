class Solution:
    def encode(self, strs):

        enc_str = ""
        for s in strs:
            enc_str += f"{len(s)}#{s}"
        return enc_str
        
    def decode(self, s):
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            
            decoded.append(s[j+1:j+1+length])
            
            i = j + 1 + length
            
        return decoded
