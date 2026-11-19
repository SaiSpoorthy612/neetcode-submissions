class Solution:

    def encode(self, strs: List[str]) -> str:
        final=[]
        for s in strs:
            final.append(str(len(s)))
            final.append('#')
            final.append(s)
        return "".join(final)

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            length=int(s[i:j])
            i=j+1
            j=i+length
            res.append(s[i:j])
            i=j
        return res
