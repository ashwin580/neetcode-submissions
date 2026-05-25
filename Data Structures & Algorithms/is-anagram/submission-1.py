class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_frequency = {}
        t_frequency = {}

        for i in range(len(s)):
            if s[i] in s_frequency:
                s_frequency[s[i]] += 1
            else:
                s_frequency[s[i]] = 1
            
            if t[i] in t_frequency:
                t_frequency[t[i]] += 1
            else:
                t_frequency[t[i]] = 1
        
        # for key in s_frequency:
        #     if key not in t_frequency:
        #         return False
        #     if s_frequency[key] != t_frequency[key]:
        #         return False
        
        return s_frequency == t_frequency
            
        