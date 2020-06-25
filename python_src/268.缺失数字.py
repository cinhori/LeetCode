#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 缺失数字
#
# https://leetcode-cn.com/problems/missing-number/description/
#
# algorithms
# Easy (55.68%)
# Likes:    271
# Dislikes: 0
# Total Accepted:    70.5K
# Total Submissions: 125.9K
# Testcase Example:  '[3,0,1]'
#
# 给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。
# 
# 
# 
# 示例 1:
# 
# 输入: [3,0,1]
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: [9,6,4,2,3,5,7,0,1]
# 输出: 8
# 
# 
# 
# 
# 说明:
# 你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?
# 
#

# @lc code=start
class Solution:
    # # 60ms, 43.96%; 14.6MB, 12.12%
    # def missingNumber(self, nums: List[int]) -> int:
    #     nums = sorted(nums)
    #     for i in range(len(nums)):
    #         if nums[i] != i: return i
    #     return nums[-1]+1

    # # 4280ms, 5.04%; 14.6MB, 12.12%
    # def missingNumber(self, nums: List[int]) -> int:
    #     for i in range(len(nums)):
    #         if i not in nums: return i
    #     return len(nums)

    # # 36ms, 98.88%; 14.5MB, 15.15% 
    # def missingNumber(self, nums: List[int]) -> int:
    #     return sum(list(range(1, len(nums)+1))) - sum(nums)

    # 56ms, 54.1%; 14.5MB, 15.15%
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)
        for i, value in enumerate(nums):
            result ^= i ^ value
        return result

# @lc code=end

