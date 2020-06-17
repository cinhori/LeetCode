#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#
# https://leetcode-cn.com/problems/contains-duplicate-ii/description/
#
# algorithms
# Easy (38.81%)
# Likes:    175
# Dislikes: 0
# Total Accepted:    48.1K
# Total Submissions: 122.9K
# Testcase Example:  '[1,2,3,1]\n3'
#
# 给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的
# 绝对值 至多为 k。
# 
# 
# 
# 示例 1:
# 
# 输入: nums = [1,2,3,1], k = 3
# 输出: true
# 
# 示例 2:
# 
# 输入: nums = [1,0,1,1], k = 1
# 输出: true
# 
# 示例 3:
# 
# 输入: nums = [1,2,3,1,2,3], k = 2
# 输出: false
# 
#

# @lc code=start
class Solution:
    # # 60ms, 30.05%; 21.4MB, 9.09%
    # # 字典
    # def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    #     nums_dict = {}
    #     for i in range(0, len(nums)):
    #         if nums[i] in nums_dict:
    #             if (i - nums_dict.get(nums[i])) <= k:
    #                 return True
    #         nums_dict[nums[i]] = i
    #     return False

    # 60ms, 30.05%; 18.2MB, 54.55%
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_set = set()
        for i in range(0, len(nums)):
            if nums[i] in nums_set: return True
            nums_set.add(nums[i])
            if len(nums_set) > k:
                nums_set.remove(nums[i-k])
        return False

# @lc code=end

