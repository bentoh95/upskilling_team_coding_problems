class Solution(object):
    def findRepeatedDnaSequences(self, s):
        if len(s) < 10:
            return []

        seen = set()
        ans = set()
        for i in range(len(s)-9):
            dna = s[i:i+10]
            if dna in seen:
                ans.add(dna)
            elif dna not in seen:
                seen.add(dna)
    
        return list(ans)

        