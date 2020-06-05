#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#
# https://leetcode-cn.com/problems/majority-element/description/
#
# algorithms
# Easy (63.30%)
# Likes:    618
# Dislikes: 0
# Total Accepted:    172.9K
# Total Submissions: 272.6K
# Testcase Example:  '[3,2,3]'
#
# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
# 
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
# 
# 
# 
# 示例 1:
# 
# 输入: [3,2,3]
# 输出: 3
# 
# 示例 2:
# 
# 输入: [2,2,1,1,1,2,2]
# 输出: 2
# 
# 
#

# @lc code=start
class Solution:
    # # 48ms, 78.15%; 15.2MB, 6.9%
    # def majorityElement(self, nums: List[int]) -> int:
    #     nums_dict = {}
    #     for num in nums:
    #         temp = nums_dict.get(num, 0) + 1
    #         nums_dict[num] = temp
    #     max_key, max_value = nums[0], 0
    #     for key, value in nums_dict.items():
    #         if value >= max_value:
    #             max_key = key
    #             max_value = value
    #     return max_key

    # 52ms, 65.41%; 14.9MB, 6.9%
    # 投票法
    def majorityElement(self, nums: List[int]) -> int:
        value, time = nums[0], 0
        for num in nums:
            if num == value:
                time += 1
            else:
                if time == 0:
                    value = num
                    time = 1
                else:
                    time -= 1
        return value

# @lc code=end

