#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#
# https://leetcode-cn.com/problems/house-robber/description/
#
# algorithms
# Easy (44.67%)
# Likes:    792
# Dislikes: 0
# Total Accepted:    114.3K
# Total Submissions: 255.7K
# Testcase Example:  '[1,2,3,1]'
#
# 
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
# 
# 给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
# 
# 示例 1:
# 
# 输入: [1,2,3,1]
# 输出: 4
# 解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
# 偷窃到的最高金额 = 1 + 3 = 4 。
# 
# 示例 2:
# 
# 输入: [2,7,9,3,1]
# 输出: 12
# 解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
# 偷窃到的最高金额 = 2 + 9 + 1 = 12 。
# 
# 
#

# @lc code=start
class Solution:
    # # Time Limit Exceeded
    # def rob(self, nums: List[int]) -> int:
    #     if not nums: return 0
    #     if len(nums) == 1: return nums[0]
    #     if len(nums) == 2: return max(nums[0], nums[1])
    #     return max(nums[0] + self.rob(nums[2:]), self.rob(nums[1:]))

    # # 32ms, 96.09%; 13.8MB, 9.09%
    # # 动态规划
    # def rob(self, nums: List[int]) -> int:
    #     if not nums: return 0
    #     if len(nums) == 1: return nums[0]
    #     if len(nums) == 2: return max(nums[0], nums[1])
    #     max_rob = [nums[0], max(nums[0], nums[1])]
    #     for i in range(2, len(nums)):
    #         max_rob.append(max(max_rob[i-1], max_rob[i-2]+nums[i]))
    #     return max_rob[-1]

    # 28ms, 99%; 13.6MB, 9.09%
    # 动态规划+滚动数组
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        size = len(nums)
        if size == 1:
            return nums[0]
        
        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, size):
            first, second = second, max(first + nums[i], second)
        
        return second

# @lc code=end

