#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#
# https://leetcode-cn.com/problems/contains-duplicate/description/
#
# algorithms
# Easy (52.36%)
# Likes:    254
# Dislikes: 0
# Total Accepted:    141.2K
# Total Submissions: 269.1K
# Testcase Example:  '[1,2,3,1]'
#
# 给定一个整数数组，判断是否存在重复元素。
# 
# 如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。
# 
# 
# 
# 示例 1:
# 
# 输入: [1,2,3,1]
# 输出: true
# 
# 示例 2:
# 
# 输入: [1,2,3,4]
# 输出: false
# 
# 示例 3:
# 
# 输入: [1,1,1,3,3,4,3,2,4,2]
# 输出: true
# 
#

# @lc code=start
class Solution:
    # # 56ms, 31.64%; 19MB, 20%
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     num_set = set()
    #     for i in nums:
    #         if i in num_set:
    #             return True
    #         else:
    #             num_set.add(i)
    #     return False

    # # Time Limit Exceeded
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     for i in range(0, len(nums)):
    #         if nums[i] in nums[:i]: return True
    #     return False

    # # 60ms, 21.66%; 19MB, 16%
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     return len(nums) > len(set(nums))

    # 48ms, 67.47%; 16.7MB, 100%
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]: return True
        return False

# @lc code=end

