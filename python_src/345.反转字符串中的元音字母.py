#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#
# https://leetcode-cn.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (49.88%)
# Likes:    97
# Dislikes: 0
# Total Accepted:    38.5K
# Total Submissions: 76.8K
# Testcase Example:  '"hello"'
#
# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
# 
# 示例 1:
# 
# 输入: "hello"
# 输出: "holle"
# 
# 
# 示例 2:
# 
# 输入: "leetcode"
# 输出: "leotcede"
# 
# 说明:
# 元音字母不包含字母"y"。
# 
#

# @lc code=start
class Solution:
    # # 68ms, 65.09%; 14.8MB, 16.67%
    # def reverseVowels(self, s: str) -> str:
    #     vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    #     start, end = 0, len(s)-1
    #     res = list(s)
    #     while start < end:
    #         while start < end and res[start] not in vowels:
    #             start += 1
    #         while start < end and res[end] not in vowels:
    #             end -= 1
    #         res[start], res[end] = res[end], res[start]
    #         start, end = start + 1, end - 1
    #     return ''.join(res)

    def reverseVowels(self, s: str) -> str:
        
# @lc code=end

