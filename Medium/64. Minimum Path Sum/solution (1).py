# 64. Minimum Path Sum

#Runtime: 100 ms, faster than 81.46% of Python3 online submissions for Minimum Path Sum.

#Memory Usage: 15.4 MB, less than 19.30% of Python3 online submissions for Minimum Path Sum.

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        sum = [[0 for _ in range(n)] for _ in range(m)]
        sum[0][0] = grid[0][0]

        for i in range(1,m):
            sum[i][0] = grid[i][0] + sum[i - 1][0]
        for j in range(1,n):
            sum[0][j] = grid[0][j] + sum[0][j - 1]

        for i in range(1,m):
            for j in range(1,n):
                sum[i][j] = min(sum[i - 1][j],sum[i][j - 1]) + grid[i][j]

        return sums[-1][-1]