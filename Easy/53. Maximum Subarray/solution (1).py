# 53. Maximum Subarray

# Runtime: 64 ms, faster than 81.39% of Python3 online submissions for Maximum Subarray.

# Memory Usage: 14.7 MB, less than 5.69% of Python3 online submissions for Maximum Subarray.


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = max_sum = nums[0]
        for i in range(1, len(nums)):
            cur_sum = max(nums[i],cur_sum + nums[i])
            max_sum = max(max_sum,cur_sum)
        return max_sum