# dfs, recursion
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        self.n = len(matchsticks)
        self.s = sum(matchsticks)
        self.m = max(matchsticks)
        self.avg = self.s//4
        if self.n < 4:
            return False
        if self.s % 4 == 1 or self.m > self.avg:
            return False
        sidelength = [0 for _ in range(4)]
        matchsticks.sort(reverse = True)        
        return self.dfs(sidelength,matchsticks,0)
    def dfs (self,sidelength,matchsticks,idx):
        if self.n == idx:
            return True
        for i in range(4):
            if sidelength[i]+ matchsticks[idx] > self.avg:
                continue
            j = i-1
            while j > -1:
                if sidelength[i] == sidelength[j]:
                    break
                j -= 1
            if j != -1:
                continue
            sidelength[i] += matchsticks[idx]
            if self.dfs(sidelength,matchsticks,idx+1):
                return True
            sidelength[i] -= matchsticks[idx]
        return False
        
