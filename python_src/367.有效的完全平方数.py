#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#
# https://leetcode-cn.com/problems/valid-perfect-square/description/
#
# algorithms
# Easy (43.35%)
# Likes:    141
# Dislikes: 0
# Total Accepted:    35.7K
# Total Submissions: 82.4K
# Testcase Example:  '16'
#
# 给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。
# 
# 说明：不要使用任何内置的库函数，如  sqrt。
# 
# 示例 1：
# 
# 输入：16
# 输出：True
# 
# 示例 2：
# 
# 输入：14
# 输出：False
# 
# 
#

# @lc code=start
class Solution:
    # # 48ms, 33.01%; 13.7MB, 11.11%
    # def isPerfectSquare(self, num: int) -> bool:
    #     if num < 0: return False
    #     if num == 0 or num == 2147488281: return True  # 2**31
    #     left, right = 0, 46341
    #     while left < right:
    #         mid = int((left+right)/2)
    #         if mid ** 2 == num: return True
    #         elif mid ** 2 < num:
    #             left = mid + 1
    #         else:
    #             right = mid - 1
    #     return True if left ** 2 == num else False

    # # 36ms, 88.17%; 13.5MB, 11.11%
    # def isPerfectSquare(self, num: int) -> bool:
    #     if num < 2: return True
    #     left, right = 2, num // 2
    #     while left <= right:
    #         x = left + (right - left) // 2
    #         guess_squared = x * x
    #         if guess_squared == num:
    #             return True
    #         if guess_squared > num:
    #             right = x - 1
    #         else:
    #             left = x + 1
    #     return False

    # # 40ms, 72.15%; 13.8MB, 11.11%
    # # 牛顿迭代法：https://leetcode-cn.com/problems/valid-perfect-square/solution/you-xiao-de-wan-quan-ping-fang-shu-by-leetcode/
    # def isPerfectSquare(self, num: int) -> bool:
    #     if num < 2: return True
        
    #     x = num // 2
    #     while x * x > num:
    #         x = (x + num // x) // 2
    #     return x * x == num

    # 48ms, 32.77%; 13.6MB, 11.11%
    def isPerfectSquare(self, num: int) -> bool:
        num1 = 1
        while num > 0: 
            num -= num1
            num1 += 2
        return num == 0

# @lc code=end

