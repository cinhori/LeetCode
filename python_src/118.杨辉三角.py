#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#
# https://leetcode-cn.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (66.47%)
# Likes:    304
# Dislikes: 0
# Total Accepted:    79.7K
# Total Submissions: 119.9K
# Testcase Example:  '5'
#
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
# 
# 
# 
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
# 
# 示例:
# 
# 输入: 5
# 输出:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
# 
#

# @lc code=start
class Solution:
    # # 32ms, 94.08%; 13.5MB, 11.76%
    # def generate(self, numRows: int) -> List[List[int]]:
    #     if numRows == 0: return []
    #     if numRows == 1: return [[1]]
    #     result = [[1],[1,1]]
    #     for i in range(3, numRows+1):
    #         last = result[i-2]
    #         now = [1,]
    #         for j in range(0, len(last)//2):
    #             now.append(last[j] + last[j+1])
    #         if len(last) % 2 == 0:
    #             rev = now[0:-1]
    #             rev.reverse()
    #             now += rev
    #         else:
    #             rev = now[:]
    #             rev.reverse()
    #             now += rev
    #         result.append(now)
    #     return result

    # 28ms, 98.5%; 13.6MB, 11.76%
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1]*(i+1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(1,i):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        return pascal

# @lc code=end

