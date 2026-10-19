class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if (len(s) != len(t)):
            return False

        s_freq = {}
        t_freq = {}

        for i in range(len(s)):
            s_freq[s[i]] = 1 + s_freq.get(s[i], 0)
            t_freq[t[i]] = 1 + t_freq.get(t[i], 0) # use .get(k, 0) when trying to increment dictionary from 0 
        return s_freq == t_freq