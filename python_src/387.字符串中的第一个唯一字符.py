#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#
# https://leetcode-cn.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (45.08%)
# Likes:    227
# Dislikes: 0
# Total Accepted:    85K
# Total Submissions: 186.3K
# Testcase Example:  '"leetcode"'
#
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
# 
# 
# 
# 示例：
# 
# s = "leetcode"
# 返回 0
# 
# s = "loveleetcode"
# 返回 2
# 
# 
# 
# 
# 提示：你可以假定该字符串只包含小写字母。
# 
#

# @lc code=start
class Solution:
    # # 560ms, 14.33%; 13.7MB, 6.67%
    # def firstUniqChar(self, s: str) -> int:
    #     if not s: return -1
    #     for i in range(len(s)-1):
    #         if s[i] not in (s[0:i] + s[i+1::]): return i
    #     return -1 if s[-1] in s[0:len(s)-1] else len(s)-1

    # # 92ms, 88.63%; 13.9MB, 6.67%
    # def firstUniqChar(self, s: str) -> int:
    #     if not s: return -1
    #     result, nodes = [], set()
    #     for c in s:
    #         if c not in nodes: 
    #             result.append(c)
    #             nodes.add(c)
    #         else: 
    #             if c in result: result.remove(c)
    #     return s.index(result[0]) if result else -1

    # 124ms, 66.06%; 13.9MB, 6.67%
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1       

# @lc code=end

