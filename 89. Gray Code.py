# write in binary format, and find the regular pattern
class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n<1:
            return 
        if n == 1:
            return [0,1]
        res = [0,1]
        for i in range(1,n):
            tmp = res[::-1]
            y = 2**i
            for x in tmp:
                res.append(x+y)       
        return res
