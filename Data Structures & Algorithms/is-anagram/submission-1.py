class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        set_s = set(s) 
        if set_s != set(t):
            return False        
        for c in set_s:
            if s.count(c) != t.count(c):
                return False            
        return True