#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#
# https://leetcode-cn.com/problems/word-pattern/description/
#
# algorithms
# Easy (42.64%)
# Likes:    161
# Dislikes: 0
# Total Accepted:    25.8K
# Total Submissions: 60.2K
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# 给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
# 
# 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。
# 
# 示例1:
# 
# 输入: pattern = "abba", str = "dog cat cat dog"
# 输出: true
# 
# 示例 2:
# 
# 输入:pattern = "abba", str = "dog cat cat fish"
# 输出: false
# 
# 示例 3:
# 
# 输入: pattern = "aaaa", str = "dog cat cat dog"
# 输出: false
# 
# 示例 4:
# 
# 输入: pattern = "abba", str = "dog dog dog dog"
# 输出: false
# 
# 说明:
# 你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。    
# 
#

# @lc code=start
class Solution:
    # # 44ms, 39.3%; 13.7MB, 10%
    # def wordPattern(self, pattern: str, str: str) -> bool:
    #     str_list = str.split()
    #     if len(str_list) != len(pattern): return False
    #     dict = {}
    #     for i in range(len(str_list)):
    #         if str_list[i] in dict.keys():
    #             if dict[str_list[i]] != pattern[i]: return False
    #         else:
    #             if pattern[i] in dict.values(): return False
    #             dict[str_list[i]] = pattern[i]
    #     return True
        
    # 40ms, 63.66%; 13.8MB, 10%
    def wordPattern(self, pattern: str, str: str) -> bool:
        res=str.split()
        return list(map(pattern.index, pattern))==list(map(res.index,res))

# @lc code=end

