#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/description/
#
# algorithms
# Easy (59.96%)
# Likes:    709
# Dislikes: 0
# Total Accepted:    161.2K
# Total Submissions: 268.7K
# Testcase Example:  '[7,1,5,3,6,4]'
#
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
# 
# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
# 
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 
# 
# 
# 示例 1:
# 
# 输入: [7,1,5,3,6,4]
# 输出: 7
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
# 随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
# 
# 
# 示例 2:
# 
# 输入: [1,2,3,4,5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
# 注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
# 因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
# 
# 
# 示例 3:
# 
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
# 
# 
# 
# 提示：
# 
# 
# 1 <= prices.length <= 3 * 10 ^ 4
# 0 <= prices[i] <= 10 ^ 4
# 
# 
#

# @lc code=start
class Solution:
    # # 808ms, 5.01%; 15.2MB, 5%
    # # 暴力解法
    # def maxProfit(self, prices: List[int]) -> int:
    #     return self._maxProfit(prices, 0, {})
    
    # def _maxProfit(self, prices, start, max_profits):
    #     """
    #     @max_profits:字典，记录已经计算的节点的最大利润
    #     """
    #     max_profit = 0
    #     for i in range(start, len(prices)): # i买入
    #         if i in max_profits.keys(): continue
    #         for j in range(i+1, len(prices)): # j卖出
    #             if j == i+1 and prices[j] <= prices[i]: break
    #             if prices[j] > prices[i]:
    #                 if j+1 not in max_profits.keys():
    #                     max_profits[j+1] = self._maxProfit(prices, j+1, max_profits)
    #                 max_profit = max(max_profit, prices[j]-prices[i] + max_profits[j+1])
    #     return max_profit

    # # 100ms, 10.66%; 14.8MB, 5%
    # def maxProfit(self, prices: List[int]) -> int:
    #     valley = prices[0]
    #     peak = prices[0]
    #     max_profit = 0
    #     i = 0
    #     while i < len(prices):
    #         while i+1 < len(prices) and prices[i] > prices[i+1]:
    #             i += 1
    #         valley = i
    #         while i+1 < len(prices) and prices[i] < prices[i+1]:
    #             i += 1
    #         peak = i
    #         max_profit += prices[peak] - prices[valley]
    #         i += 1
    #     return max_profit
        
    # 72ms, 52.26%; 15MB, 5%
    # 贪心算法：每一步都做出当时看起来的最优解，以此获得全局的最优解
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                max_profit += prices[i+1] - prices[i]
        return max_profit

    # 动态规划：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/solution/tan-xin-suan-fa-by-liweiwei1419-2/
# @lc code=end

