#62. Unique Paths

#Runtime: 32 ms, faster than 50.25% of Python3 online submissions for Unique Paths.

#Memory Usage: 13.8 MB, less than 5.77% of Python3 online submissions for Unique Paths.


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        count = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    count[i][j] = 1
                else:
                    count[i][j]= count[i - 1][j] + count[i][j - 1]
        return count[m - 1][n - 1]