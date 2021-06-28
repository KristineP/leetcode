# solution: two stacks
class Solution:
    def removeDuplicates(self, s: str) -> str:
        if not s:
            return
        a = list(s)
        b = []
        while a:
            if b and b[-1]==a[0]:
                a.pop(0)
                b.pop()
            else:
                b.append(a.pop(0))
        return ''.join(b)
