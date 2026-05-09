class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            for ch in set(s):
                if t.count(ch) != s.count(ch):
                    return False
            return True