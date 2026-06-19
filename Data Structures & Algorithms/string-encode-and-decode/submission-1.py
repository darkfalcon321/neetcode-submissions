class Solution:

    def encode(self, strs: List[str]) -> str:
        new_strs = ""
        for s in strs:
            new_strs += str(len(s)) + "#" + s
        return new_strs

    def decode(self, s: str) -> List[str]:
        new_strs, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            new_strs.append(s[j+1 : j+1+length])

            i = j + 1 + length

        return new_strs
