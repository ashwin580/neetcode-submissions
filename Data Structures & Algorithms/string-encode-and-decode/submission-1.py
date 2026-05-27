class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:

        list_result = []
        print(s)

        current = 0
        while current < len(s):
            j = current

            while s[j] != '#':
                j += 1

            length = int(s[current:j])
            list_result.append(s[j+1:j+1+length])
            current = j+1+length
        
        return list_result




