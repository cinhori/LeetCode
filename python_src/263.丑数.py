#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#
# https://leetcode-cn.com/problems/ugly-number/description/
#
# algorithms
# Easy (49.19%)
# Likes:    130
# Dislikes: 0
# Total Accepted:    34.9K
# Total Submissions: 70.8K
# Testcase Example:  '6'
#
# 编写一个程序判断给定的数是否为丑数。
# 
# 丑数就是只包含质因数 2, 3, 5 的正整数。
# 
# 示例 1:
# 
# 输入: 6
# 输出: true
# 解释: 6 = 2 × 3
# 
# 示例 2:
# 
# 输入: 8
# 输出: true
# 解释: 8 = 2 × 2 × 2
# 
# 
# 示例 3:
# 
# 输入: 14
# 输出: false 
# 解释: 14 不是丑数，因为它包含了另外一个质因数 7。
# 
# 说明：
# 
# 
# 1 是丑数。
# 输入不会超过 32 位有符号整数的范围: [−2^31,  2^31 − 1]。
# 
# 
#

# @lc code=start
class Solution:
    # # 48ms, 43.17%; 13.8MB, 5.56%
    # def isUgly(self, num: int) -> bool:
    #     if num <= 0:
    #         return False
    #     result = num
    #     while result != 1:
    #         if result % 2 == 0:
    #             result = result / 2
    #         elif result % 3 == 0:
    #             result = result / 3
    #         elif result % 5 == 0:
    #             result = result / 5
    #         else:
    #             return False
    #     return True

    # 44ms, 65.72%; 13.6MB, 5.56%
    def isUgly(self, num: int) -> bool:
        for p in 2, 3, 5:
            while num % p == 0 and num:
                num /= p
        return num == 1

# @lc code=end

