#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#
# https://leetcode-cn.com/problems/find-the-difference/description/
#
# algorithms
# Easy (61.83%)
# Likes:    140
# Dislikes: 0
# Total Accepted:    31K
# Total Submissions: 49.8K
# Testcase Example:  '"abcd"\n"abcde"'
#
# 给定两个字符串 s 和 t，它们只包含小写字母。
# 
# 字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
# 
# 请找出在 t 中被添加的字母。
# 
# 
# 
# 示例:
# 
# 输入：
# s = "abcd"
# t = "abcde"
# 
# 输出：
# e
# 
# 解释：
# 'e' 是那个被添加的字母。
# 
# 
#

# @lc code=start
class Solution:
    # # 48ms, 48.08%; 13.8MB, 5.19%
    # def findTheDifference(self, s: str, t: str) -> str:
    #     s_dict = {}
    #     for single in s:
    #         s_dict[single] = s_dict.get(single, 0) + 1
    #     for single in t:
    #         if single in s_dict:
    #             if s_dict[single] <= 0: return single
    #             s_dict[single] = s_dict[single] - 1
    #         else:
    #             return single
    #     return -1

    # 44ms, 71.79%; 13.5MB, 89.29%;
    # 异或
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0
        for r in s: result ^= ord(r)
        for r in t: result ^= ord(r)
        return chr(result)
        
# @lc code=end

