# 给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。
# 如果不存在最后一个单词，请返回 0 。
# 说明：一个单词是指仅由字母组成、不包含任何空格字符的 最大子字符串。
# 
# 示例:
# 输入: "Hello World"
# 输出: 5


class Solution:
    # 28ms, 97.48%; 13.8MB, 5.26%
    def lengthOfLastWord(self, s):
        return len(s.strip().split(' ')[-1])

    # 28ms, 97.48%; 13.8MB, 5.26%
    def lengthOfLastWord2(self, s):
        if s.strip == '': return 0
        result = 0
        label = True
        for val in s[::-1]:
            if val == ' ' and label: continue
            if val == ' ' and not label: return result
            result += 1
            label = False
        return result


if __name__ == "__main__":
    print(Solution().lengthOfLastWord2('Hello'))