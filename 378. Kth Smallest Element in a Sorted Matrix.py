class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        if n*n < k:
            return
        def check(x):
            j = n - 1
            cnt = 0
            for i in range(n):
                while j>=0 and matrix[i][j] > x:
                    j-=1
                cnt +=j+1
            return cnt
            return cnt
        left,right = matrix[0][0], matrix[-1][-1]
        ans = 0
        while left <= right:
            mid = left + (right-left)//2
            if check(mid) >= k:
                ans = mid
                right = mid -1
            elif check(mid) < k:
                left = mid + 1
        return ans
