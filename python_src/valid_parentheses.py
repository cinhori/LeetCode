# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。
# 
# 示例 1:
# 输入: "()"
# 输出: true
# 示例 2:
# 输入: "()[]{}"
# 输出: true
# 示例 3:
# 输入: "(]"
# 输出: false
# 示例 4:
# 输入: "([)]"
# 输出: false
# 示例 5:
# 输入: "{[]}"
# 输出: true


class Solution:
    # 36ms, 84.19%; 13.7MB, 5.22%   
    def isValid(self, str):
        hashmap = {'{':1, '}':6, '(':2, ')':5, '[':3, ']':4}
        result = []
        for s in str:
            if hashmap[s] < 4: 
                result.append(s)
            else:
                if result == []: return False # 排除[']']
                tmp = result.pop()
                if hashmap[tmp] + hashmap[s] != 7:
                    return False
        
        return len(result) == 0

    # 44ms, 51.93%; 13.6MB, 5.22%
    def isValid2(self, s):
        dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in dic: stack.append(c)
            elif dic[stack.pop()] != c: return False 
        return len(stack) == 1


if __name__ == "__main__":
    print(Solution().isValid("[]]"))