class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_li = []
        t_li = []

        for i in s:
            s_li.append(i)
        s_li.sort()

        for j in t:
            t_li.append(j)
        t_li.sort()

        return s_li == t_li