#62. Unique Paths

#Runtime: 32 ms, faster than 50.25% of Python3 online submissions for Unique Paths.

#Memory Usage: 14.1 MB, less than 5.77% of Python3 online submissions for Unique Paths.


class Solution:
    def __init__(self)->None:
        self._count = None

    def uniquePaths(self, m: int, n: int) -> int:
        self._count = [[0 for _ in range(n)] for _ in range(m)]
        return self._uniquePaths(m - 1,n - 1)

    def _uniquePaths(self, i: int, j: int) -> int:
        if i < 0 or j < 0:
            return 0
        elif i == 0 or j == 0:
            return 1
        elif self._count[i][j] != 0:
            return self._count[i][j]
        
        self._count[i][j] = self._uniquePaths(i - 1, j) + self._uniquePaths(i, j - 1)
        return self._count[i][j]