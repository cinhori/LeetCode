#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#
# https://leetcode-cn.com/problems/valid-anagram/description/
#
# algorithms
# Easy (59.93%)
# Likes:    205
# Dislikes: 0
# Total Accepted:    109.6K
# Total Submissions: 181.9K
# Testcase Example:  '"anagram"\n"nagaram"'
#
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
# 
# 示例 1:
# 
# 输入: s = "anagram", t = "nagaram"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: s = "rat", t = "car"
# 输出: false
# 
# 说明:
# 你可以假设字符串只包含小写字母。
# 
# 进阶:
# 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
# 
#

# @lc code=start
class Solution:
    # # 288ms, 5.09%; 13.9MB, 8.33%
    # def isAnagram(self, s: str, t: str) -> bool:
    #     result = s
    #     for t_char in t:
    #         if t_char in result:
    #             result = result.replace(t_char, '*', 1)
    #         else:
    #             return False
    #     return True if result == '*' * len(t) else False

    # # 68ms, 43.47%; 13.8MB, 8.33%
    # def isAnagram(self, s: str, t: str) -> bool:
    #     dict = {}
    #     for s_char in s:
    #         dict[s_char] = dict.get(s_char, 0) + 1

    #     for t_char in t:
    #         if dict.get(t_char, 0) == 0:
    #             return False
    #         else:
    #             dict[t_char] = dict.get(t_char) - 1
        
    #     for value in dict.values():
    #         if value != 0: return False
    #     return True

    # 56ms, 78.28%; 14.7MB, 8.33%
    def isAnagram(self, s: str, t: str) -> bool:
        return True if sorted(s) == sorted(t) else False

# @lc code=end

