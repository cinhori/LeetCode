#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#
# https://leetcode-cn.com/problems/happy-number/description/
#
# algorithms
# Easy (60.12%)
# Likes:    363
# Dislikes: 0
# Total Accepted:    81.9K
# Total Submissions: 136.3K
# Testcase Example:  '19'
#
# 编写一个算法来判断一个数 n 是不是快乐数。
# 
# 「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到
# 1。如果 可以变为  1，那么这个数就是快乐数。
# 
# 如果 n 是快乐数就返回 True ；不是，则返回 False 。
# 
# 
# 
# 示例：
# 
# 输入：19
# 输出：true
# 解释：
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
# 
# 
#

# @lc code=start
class Solution:
    # # 40ms, 13.44%; 13.8MB, 9.09%
    # def isHappy(self, n: int) -> bool:
    #     def get_next(num):
    #         sum = 0
    #         while num > 0:
    #             sum += (num % 10) ** 2
    #             num = num // 10
    #         return sum

    #     num_set = set()
    #     while True:
    #         if n == 1: return True
    #         if n in num_set: return False
    #         num_set.add(n)
    #         n = get_next(n)
        
    # 链表找环，快慢指针
    # 52ms, 29.7%; 13.6MB, 29.7%
    def isHappy(self, n: int) -> bool:
        def get_next(num):
            sum = 0
            while num > 0:
                sum += (num % 10) ** 2
                num = num // 10
            return sum

        slow, fast = n, get_next(n)
        while slow != 1 and fast != 1:
            if slow == fast: return False
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        return True


# @lc code=end
