# find the closest number and the index
# narrow down the window to [idx-k,idx+k+1]
# narrow down to k numbers
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if not arr:
            return
        if x<=arr[0]:
            return arr[:k]
        if x>=arr[-1]:
            return arr[-k:] if k<=len(arr) else arr
        m = arr[0]
        for i in range(1,len(arr)):
            if abs(m-x)>abs(arr[i]-x):
                m = arr[i]
        l = arr.index(m)-k if arr.index(m)-k>=0 else 0
        r = arr.index(m)+k if arr.index(m)+k<len(arr) else len(arr)-1
        while r-l>=k:
            if abs(x-arr[l])>abs(arr[r]-x):
                l+=1
            else:
                r-=1
        return arr[l:r+1]
