#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#
# https://leetcode-cn.com/problems/count-primes/description/
#
# algorithms
# Easy (33.71%)
# Likes:    367
# Dislikes: 0
# Total Accepted:    60.4K
# Total Submissions: 177.9K
# Testcase Example:  '10'
#
# 统计所有小于非负整数 n 的质数的数量。
# 
# 示例:
# 
# 输入: 10
# 输出: 4
# 解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
# 
# 
#

# @lc code=start
class Solution:
    # # time limit exceeded, 499979, 17/20
    # def countPrimes(self, n: int) -> int:
    #     if n <= 2: return 0
    #     prime_nums = [2]
    #     for i in range(3, n, 2):
    #         tag = False
    #         for j in prime_nums[1:]:
    #             if j*j > i: break
    #             if i % j == 0: 
    #                 tag = True
    #                 break
    #         if tag == False: prime_nums.append(i)
    #     return len(prime_nums)
            
    # # 1196ms, 24.03%; 25.2MB, 68.75%
    # # 标记：Sieve of Eratosthenes法
    # def countPrimes(self, n: int) -> int:
    #     if n <= 2: return 0
    #     prime_nums = [True] * n
    #     prime_nums[0], prime_nums[1] = False, False
    #     result = 0
    #     for i in range(2, n):
    #         if prime_nums[i] == True:
    #             j = 2
    #             result += 1
    #             while i * j < n:
    #                 prime_nums[i*j] = False
    #                 j += 1
    #     return result

    # 680ms, 40.18; 25.2MB, 68.75%;
    def countPrimes(self, n: int) -> int:
        if n <= 2: return 0
        prime_nums = [True] * n
        prime_nums[0], prime_nums[1] = False, False
        result, i = 0, 2
        while i*i < n:
            if prime_nums[i]:
                j = i * i
                while j < n:
                    prime_nums[j] = False
                    j += i
            i += 1

        for i in range(2, n):
            if prime_nums[i]: result += 1
        return result
        


# @lc code=end

