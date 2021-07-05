func matrixReshape(mat [][]int, r int, c int) [][]int {
    if mat == nil{
        return nil
    }
    n := len(mat)
    m := len(mat[0])
    if n * m != r * c {
        return mat
    }
    ans := make([][]int, r)
    for i := 0; i < n; i++{
        for j := 0; j < m; j++{
            tmp := i * m + j
            var x int = tmp / c
            var y int = tmp % c
            if y == 0{
                ans[x] = make([]int, c)
            }
            ans[x][y] = mat[i][j]
        }
    }
    return ans
}
