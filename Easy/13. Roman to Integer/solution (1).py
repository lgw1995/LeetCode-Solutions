# 13. Roman to Integer

# Runtime: 40 ms, faster than 90.29% of Python3 online submissions for Roman to Integer.
# Memory Usage: 13.8 MB, less than 5.38% of Python3 online submissions for Roman to Integer.


class Solution:
    _NUM_MAP = {'I':1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

    def romanToInt(self, s: str) -> int:
        if len(s) == 0:
            return 0

        prev = Solution._NUM_MAP[s[0]]
        sum  = prev
        for i in range(1, len(s)):
            curr = Solution._NUM_MAP[s[i]]
            sum += curr
            if curr > prev:
                sum -= prev * 2
            prev = curr
        return sum