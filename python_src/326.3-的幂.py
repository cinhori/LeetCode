#
# @lc app=leetcode.cn id=326 lang=python3
#
# [326] 3的幂
#
# https://leetcode-cn.com/problems/power-of-three/description/
#
# algorithms
# Easy (46.86%)
# Likes:    110
# Dislikes: 0
# Total Accepted:    49.1K
# Total Submissions: 104.7K
# Testcase Example:  '27'
#
# 给定一个整数，写一个函数来判断它是否是 3 的幂次方。
# 
# 示例 1:
# 
# 输入: 27
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: 0
# 输出: false
# 
# 示例 3:
# 
# 输入: 9
# 输出: true
# 
# 示例 4:
# 
# 输入: 45
# 输出: false
# 
# 进阶：
# 你能不使用循环或者递归来完成本题吗？
# 
#

# @lc code=start
class Solution:
    # # 88ms, 81.14%; 13.7MB, 9.09%
    # def isPowerOfThree(self, n: int) -> bool:
    #     while n >= 3:
    #         if n % 3 != 0: return False
    #         n = n / 3
    #     return n == 1
        
    # 140ms, 13.36%; 13.6MB, 9.09%
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False
        res = math.log(n, 3)
        # error: res == int(res) for 243
        return True if n == 3**round(res) else False

# @lc code=end

