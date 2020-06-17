#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#
# https://leetcode-cn.com/problems/power-of-two/description/
#
# algorithms
# Easy (48.07%)
# Likes:    206
# Dislikes: 0
# Total Accepted:    63.6K
# Total Submissions: 131.8K
# Testcase Example:  '1'
#
# 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
# 
# 示例 1:
# 
# 输入: 1
# 输出: true
# 解释: 2^0 = 1
# 
# 示例 2:
# 
# 输入: 16
# 输出: true
# 解释: 2^4 = 16
# 
# 示例 3:
# 
# 输入: 218
# 输出: false
# 
#

# @lc code=start
class Solution:
    # # 48ms, 41.24%; 13.6MB, 6.25%
    # def isPowerOfTwo(self, n: int) -> bool:
    #     if n < 1: return False
    #     while n != 1:
    #         if n % 2 == 1: return False
    #         n = n / 2
    #     return True

    # # 36ms, 93.51%; 13.6MB, 6.25%
    # # 知识点：补码表示 -n = -n+1
    # def isPowerOfTwo(self, n: int) -> bool:
    #     if n < 1: return False
    #     return n & (-n) == n

    # 40ms, 82.12%; 13.7MB, 6.25%
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1: return False
        return n & (n-1) == 0

# @lc code=end

