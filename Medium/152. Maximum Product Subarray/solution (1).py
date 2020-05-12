# 152. Maximum Product Subarray

# Runtime: 52 ms, faster than 82.77% of Python3 online submissions for Maximum Product Subarray.
# Memory Usage: 14.2 MB, less than 17.24% of Python3 online submissions for Maximum Product Subarray.


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_large_prdct = cur_small_prdct = max_prdct = nums[0]
        
        for i in range(1, len(nums)):
            
            if nums[i] >= 0:
                cur_large_prdct = max(nums[i],cur_large_prdct * nums[i])
                cur_small_prdct = min(nums[i],cur_small_prdct * nums[i])
            else:
                temp = cur_large_prdct
                cur_large_prdct = max(nums[i],cur_small_prdct * nums[i])
                cur_small_prdct = min(nums[i],temp * nums[i])

            max_prdct = max(max_prdct,cur_large_prdct)
        return max_prdct