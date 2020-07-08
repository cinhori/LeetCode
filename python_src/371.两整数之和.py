#
# @lc app=leetcode.cn id=371 lang=python3
#
# [371] 两整数之和
#
# https://leetcode-cn.com/problems/sum-of-two-integers/description/
#
# algorithms
# Easy (54.76%)
# Likes:    270
# Dislikes: 0
# Total Accepted:    31.3K
# Total Submissions: 56.6K
# Testcase Example:  '1\n2'
#
# 不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。
# 
# 示例 1:
# 
# 输入: a = 1, b = 2
# 输出: 3
# 
# 
# 示例 2:
# 
# 输入: a = -2, b = 3
# 输出: 1
# 
#

# @lc code=start
class Solution:
    # # 40ms, 60.11%; 13.8MB, 16.67%
    # def getSum(self, a: int, b: int) -> int:
    #     return sum([a, b])

    # 36ms, 82.64%; 13.7MB, 16.67%
    # 位运算https://leetcode-cn.com/problems/sum-of-two-integers/solution/wei-yun-suan-xiang-jie-yi-ji-zai-python-zhong-xu-y/
    def getSum(self, a: int, b: int) -> int:
        MASK = 0x100000000
        # 整型最大值
        MAX_INT = 0x7FFFFFFF
        MIN_INT = MAX_INT + 1
        while b != 0:
            # 计算进位
            carry = (a & b) << 1 
            # 取余范围限制在 [0, 2^32-1] 范围内
            a = (a ^ b) % MASK
            b = carry % MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)  
        
# @lc code=end

