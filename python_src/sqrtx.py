# 实现 int sqrt(int x) 函数。
# 计算并返回 x 的平方根，其中 x 是非负整数。
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
# 
# 示例 1:
# 输入: 4
# 输出: 2
# 示例 2:
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842..., 
# 由于返回类型是整数，小数部分将被舍去。


import math


class Solution:
    # 3812ms, 5.97%; 13.7MB, 6.06%
    def mySqrt(self, x):
        i = 1
        while True:
            if i * i == x:
                return i
            elif i * i > x:
                return i-1
            else:
                i += 1

    # 32ms, 99.04%; 13.7MB, 6.06%
    # 注意：浮点数计算结果有误差
    def mySqrt2(self, x):
        if x == 0: return 0
        res = int(math.exp(0.5 * math.log(x)))
        if (res+1) ** 2 <= x: return res+1
        else: return res

    # 二分查找
    # 60ms, 32.84%; 13.6MB, 6.06%
    def mySqrt3(self, x):
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l + r) // 2
            if mid ** 2 == x: return mid
            if mid ** 2 < x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans


if __name__ == "__main__":
    print(Solution().mySqrt2(2147395600))