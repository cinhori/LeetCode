# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。
# 
# 示例 1:
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 示例 2:
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 说明:
# 所有输入只包含小写字母 a-z 。


class Solution:
    # 40ms, 73.72%; 13.8MB, 6.15%
    def longestCommonPrefix(self, strs):
        if len(strs) == 0: return ''
        min = len(strs[0])
        for str in strs:
            min = min if min <= len(str) else len(str)
        result = ''
        
        for i in range(1, min+1):
            prefix = strs[0][0:i]
            for j in range(1, len(strs)):
                if not strs[j].startswith(prefix):
                    return result
            result = prefix
        return result

    # 52ms, 26.57%; 13.7MB, 6.15%
    def longestCommonPrefix2(self, strs):
        if len(strs) == 0:
            return ''
        s = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(s) != 0 :
                s = s[:-1]
        return s


if __name__ == "__main__":
    print(Solution().longestCommonPrefix2(["flower","flow","flight"]))
