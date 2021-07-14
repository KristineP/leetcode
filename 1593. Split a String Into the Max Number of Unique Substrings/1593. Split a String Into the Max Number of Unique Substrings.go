// backtrack
func maxUniqueSplit(s string) int {
    if s == "" {
        return 0
    }
    dic := make(map[string]int)
    return backtrack(s,dic)
}
func backtrack(s string, dic map[string]int) int {
    ans := 0
    if s != "" {
        for i:=1;i<len(s)+1;i++{
            tmp := s[:i]
            _,ok := dic[tmp]
            if !ok{
                dic[tmp] = 1
                bt := 1+backtrack(s[i:],dic)
                if bt > ans{
                    ans = bt
                }
                delete(dic,tmp)
            }
        }
    }
    return ans
}
