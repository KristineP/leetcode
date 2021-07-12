func canPartition(nums []int) bool {
    sum := 0
    for _,num := range nums {
        sum += num
    }
    if sum & 1 == 1 {
        return false
    }
    s := int(sum/2)
    dp := make([]bool,s+1)
    dp[0] = true
    for _,num := range nums{
        for i := s; i>0;i-- {
            if i>=num {
                dp[i] = dp[i] || dp[i-num]
            }
        }
    }
    return dp[s]
}
