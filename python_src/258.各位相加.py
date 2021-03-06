#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#
# https://leetcode-cn.com/problems/add-digits/description/
#
# algorithms
# Easy (66.64%)
# Likes:    250
# Dislikes: 0
# Total Accepted:    41.5K
# Total Submissions: 62K
# Testcase Example:  '38'
#
# 给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。
# 
# 示例:
# 
# 输入: 38
# 输出: 2 
# 解释: 各位相加的过程为：3 + 8 = 11, 1 + 1 = 2。 由于 2 是一位数，所以返回 2。
# 
# 
# 进阶:
# 你可以不使用循环或者递归，且在 O(1) 时间复杂度内解决这个问题吗？
# 
#

# @lc code=start
class Solution:
    # # 40ms, 84.3%; 13.6MB, 8.7%
    # def addDigits(self, num: int) -> int:
    #     result = num
    #     while result > 9:
    #         temp = str(result)
    #         result = int(temp[0]) + int(temp[1:])
    #     return result

    # 36ms, 94.21%; 13.6MB, 8.7%
    def addDigits(self, num: int) -> int:
        return num if num < 10 else (num - 1) % 9 + 1

# @lc code=end