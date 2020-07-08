#
# @lc app=leetcode.cn id=374 lang=python3
#
# [374] 猜数字大小
#
# https://leetcode-cn.com/problems/guess-number-higher-or-lower/description/
#
# algorithms
# Easy (44.14%)
# Likes:    64
# Dislikes: 0
# Total Accepted:    25.7K
# Total Submissions: 57.6K
# Testcase Example:  '10\n6'
#
# 我们正在玩一个猜数字游戏。 游戏规则如下：
# 我从 1 到 n 选择一个数字。 你需要猜我选择了哪个数字。
# 每次你猜错了，我会告诉你这个数字是大了还是小了。
# 你调用一个预先定义好的接口 guess(int num)，它会返回 3 个可能的结果（-1，1 或 0）：
# 
# -1 : 我的数字比较小
# ⁠1 : 我的数字比较大
# ⁠0 : 恭喜！你猜对了！
# 
# 
# 
# 
# 示例 :
# 
# 输入: n = 10, pick = 6
# 输出: 6
# 
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    # # 48ms, 18.1%; 13.5MB, 10%
    # # 二分查找
    # def guessNumber(self, n: int) -> int:
    #     small, big = 1, n
    #     while small < big:
    #         mid = (small + big) // 2
    #         if guess(mid) == 0: return mid
    #         elif guess(mid) == -1:
    #             big = mid - 1
    #         else:
    #             small = mid + 1
    #     return small if guess(small) == 0 else small

    # 36ms, 85.98%; 13.7MB, 10%
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        while low <= high:
            mid1 = low + (high - low) // 3
            mid2 = high - (high - low) // 3
            flag1 = guess(mid1)
            flag2 = guess(mid2)
            if flag1 == 0: return mid1
            if flag2 == 0: return mid2
            if flag1 < 0: high = mid1 - 1
            elif flag2 > 0: low = mid2 + 1
            else:
                low = mid1 + 1
                high = mid2 - 1
        return -1
        
# @lc code=end

