# 1. Two Sum

# Runtime: 44 ms, faster than 91.98% of Python3 online submissions for Two Sum.

# Memory Usage: 15.4 MB, less than 5.11% of Python3 online submissions for Two Sum.


from typing import List

class Solution:
    # One-pass Hash Table
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dict:
                return dict[complement], i
            else:
                dict[nums[i]] = i
        assert False