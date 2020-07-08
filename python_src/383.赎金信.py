#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#
# https://leetcode-cn.com/problems/ransom-note/description/
#
# algorithms
# Easy (53.27%)
# Likes:    101
# Dislikes: 0
# Total Accepted:    24.7K
# Total Submissions: 45.8K
# Testcase Example:  '"a"\n"b"'
#
# 给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串 ransom 能不能由第二个字符串 magazines
# 里面的字符构成。如果可以构成，返回 true ；否则返回 false。
# 
# (题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。杂志字符串中的每个字符只能在赎金信字符串中使用一次。)
# 
# 
# 
# 注意：
# 
# 你可以假设两个字符串均只含有小写字母。
# 
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true
# 
# 
#

# @lc code=start
class Solution:
    # # 80ms, 40.75%; 13.7MB, 11.11%
    # # 哈希
    # def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    #     dict = {}
    #     for i in magazine:
    #         dict[i] = dict.get(i, 0) + 1
    #     for s in ransomNote:
    #         if dict.get(s, 0) == 0:
    #             return False
    #         else:
    #             dict[s] -= 1
    #     return True

    # # 100ms, 19.69%; 13.7MB, 11.11%
    # def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    #     magazine_array = [0] * 26
    #     for c in magazine:
    #         magazine_array[ord(c) - ord('a')] += 1
    #     for c in ransomNote:
    #         temp = ord(c) - ord('a')
    #         if magazine_array[temp] == 0:
    #             return False
    #         else:
    #             magazine_array[temp] -= 1
    #     return True

    # 48ms, 95.38%; 13.5MB, 11.11%
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in range(len(ransomNote)):
            if ransomNote[i] in magazine:
                magazine = magazine.replace(ransomNote[i],"",1)
            else:
                return False
        return True

# @lc code=end

