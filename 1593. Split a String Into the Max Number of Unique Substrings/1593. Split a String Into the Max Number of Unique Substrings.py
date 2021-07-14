# backtrack
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        if not s:
            return 0
        seen = set()
        return self.backtrack(seen,s)
    def backtrack(self,seen,s):
        ans = 0
        if s:
            for i in range(1,len(s)+1):
                tmp = s[:i]
                if tmp not in seen:
                    seen.add(tmp)
                    ans = max(ans,1+self.backtrack(seen,s[i:]))
                    seen.remove(tmp)
        return ans
