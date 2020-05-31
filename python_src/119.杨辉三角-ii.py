#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#
# https://leetcode-cn.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (61.10%)
# Likes:    148
# Dislikes: 0
# Total Accepted:    52.8K
# Total Submissions: 86.5K
# Testcase Example:  '3'
#
# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
# 
# 
# 
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
# 
# 示例:
# 
# 输入: 3
# 输出: [1,3,3,1]
# 
# 
# 进阶：
# 
# 你可以优化你的算法到 O(k) 空间复杂度吗？
# 
#

# @lc code=start
class Solution:
    # # 40ms, 68.83%; 13.7MB, 11.11%
    # def getRow(self, rowIndex: int) -> List[int]:
    #     res = [1] * (rowIndex+1)
    #     for i in range(2, rowIndex+1):
    #         last = res[0]
    #         for j in range(1, i):
    #             temp = res[j]
    #             res[j] += last
    #             last = temp
    #     return res

    # 36ms, 86.65%; 13.4MB, 11.11%
    def getRow(self, rowIndex: int) -> List[int]:
        r = [1]
        for i in range(1, rowIndex + 1):
            r.insert(0, 0)
            # 因为i行的数据长度为i+1, 所以j+1不会越界, 并且最后一个1不会被修改.
            for j in range(i):
                r[j] = r[j] + r[j + 1]
        return r
# @lc code=end

