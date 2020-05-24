# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 注意：给定 n 是一个正整数。
# 
# 示例 1：
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
# 示例 2：
# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶


class Solution:
    def __init__(self):
        self.memo = {}
    
    # 暴力递归
    # timeout
    def climbStairs(self, n):
        return self._climbStairs(0, n)

    def _climbStairs(self, i, n):
        # i为当前阶数， n为总阶数
        if i > n: return 0
        if i == n: return 1
        return self._climbStairs(i+1, n) + self._climbStairs(i+2, n)

    # 递归，记忆冗余
    # 44ms, 39.37%; 13.8MB, 20.59%
    def climbStairs2(self, n):
        return self._climbStairs2(0, n)

    def _climbStairs2(self, i, n):
        if i > n: return 0
        if i == n: return 1
        if i in self.memo.keys(): return self.memo[i]
        self.memo[i] = self._climbStairs2(i+1, n) + self._climbStairs2(i+2, n)
        return self.memo[i]

    # 动态规划
    # 28ms, 97.76%; 13.7MB, 20.59%
    def climbStairs3(self, n):
        dp = [0, 1, 2]
        if n <= 2: return dp[n]
        for i in range(3, n+1):
            dp.append(dp[i-1] + dp[i-2])
        return dp[n]

    # 斐波那契数列
    # 44ms, 39.37%; 13.7MB, 20.59%
    def climbStairs4(self, n):
        if n == 1: return 1
        first = 1
        second = 2
        for i in range(3, n+1):
            third = first + second
            first = second
            second = third
        
        return second


if __name__ == "__main__":
    print(Solution().climbStairs2(3))