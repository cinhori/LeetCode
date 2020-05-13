# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
# 
# 示例 1:
# 输入: 121
# 输出: true
# 示例 2:
# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
# 示例 3:
# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。


class Solution:
    # 76ms, 80.91%, 13.6MB, 5.88%
    def isPalindrome(self, x):
        x_str = str(x)
        return x_str[::-1] == str(x)

    #108ms, 23.87%, 13.6MB, 5.88%
    def isPalindrome2(self, x):
        if x < 0: return False
        x_reverse = 0
        x_origin = x
        while x_origin > 0:
            x_reverse = x_reverse * 10 + (x_origin%10)
            x_origin = int(x_origin/10)

        return x_reverse == x


if __name__ == "__main__":
    print(Solution().isPalindrome2(121))
