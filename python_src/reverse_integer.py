# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 
# 示例 1:
# 输入: 123
# 输出: 321
# 示例 2:
# 输入: -123
# 输出: -321
# 示例 3:
# 输入: 120
# 输出: 21
# 
# 注意:
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。


import re


class Solution:
    # 52ms, 26.91%; 13.7MB, 5.44%
    def reverse(self, x):
        if re.match(r'^\-\d+', str(x)): result = int('-'+str(x)[-1:0:-1])
        if re.match(r'^\d+', str(x)): result = int(str(x)[-1:0-(len(str(x))+1):-1])

        return result if -2147483648 < result < 2147483647 else 0

    # 44ms, 58.91%; 13.5MB, 6.67% 
    def reverse1(self, x: int) -> int:
        if re.match(r'^\-\d+', str(x)): result = int('-'+str(x)[:0:-1])
        if re.match(r'^\d+', str(x)): result = int(str(x)[::-1])
        return result if -2147483648 < result < 2147483647 else 0

    # 48ms, 30.26%; 13.7MB, 5.44%
    def reverse2(self, x: int) -> int:
        if -10 < x < 10:
            return x
        str_x = str(x)
        if str_x[0] != "-":
            str_x = str_x[::-1]
            x = int(str_x)
        else:
            str_x = str_x[:0:-1]
            x = int(str_x)
            x = -x
        return x if -2147483648 < x < 2147483647 else 0

    # 52ms, 26.83%; 13.6MB, 6.67%
    def reverse3(self, x: int) -> int:
        y, res = abs(x), 0
        # 则其数值范围为 [−2^31,  2^31 − 1]
        boundry = (1<<31) -1 if x>0 else 1<<31
        while y != 0:
            res = res*10 +y%10
            if res > boundry :
                return 0
            y //=10
        return res if x >0 else -res


if __name__ == "__main__":
    print(Solution().reverse2(-1234))