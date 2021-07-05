class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if not mat:
            return
        n = len(mat)
        m = len(mat[0])
        if n*m != r*c:
            return mat
        ans = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(n):
            for j in range(m):
                tmp = i*m + j
                x = int(tmp/c)
                y = int(tmp%c)
                ans[x][y] = mat[i][j]
        return ans
                
