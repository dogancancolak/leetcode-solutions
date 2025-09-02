class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        s_map = dict()
        t_map = dict()
        for i in range(len(s)):
            char_pos = s_map.get(s[i], [])
            char_pos.append(i)
            s_map[s[i]] = char_pos
            char_pos = t_map.get(t[i], [])
            char_pos.append(i)
            t_map[t[i]] = char_pos
        for i in range(len(s)):
            if s_map.get(s[i]) != t_map.get(t[i]):
                return False
        return True