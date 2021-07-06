from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        if not arr:
            return
        dic = Counter(arr)
        tmp = sorted(dic.items(), key=lambda item: item[1],reverse = True)
        length = int(len(arr)//2)
        n = 0
        size = 0
        for i in range(len(tmp)):
            n+=tmp[i][1]
            size +=1
            if n>= length:
                return size
