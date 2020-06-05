#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#
# https://leetcode-cn.com/problems/excel-sheet-column-title/description/
#
# algorithms
# Easy (37.72%)
# Likes:    225
# Dislikes: 0
# Total Accepted:    27.1K
# Total Submissions: 71.7K
# Testcase Example:  '1'
#
# 给定一个正整数，返回它在 Excel 表中相对应的列名称。
# 
# 例如，
# 
# ⁠   1 -> A
# ⁠   2 -> B
# ⁠   3 -> C
# ⁠   ...
# ⁠   26 -> Z
# ⁠   27 -> AA
# ⁠   28 -> AB 
# ⁠   ...
# 
# 
# 示例 1:
# 
# 输入: 1
# 输出: "A"
# 
# 
# 示例 2:
# 
# 输入: 28
# 输出: "AB"
# 
# 
# 示例 3:
# 
# 输入: 701
# 输出: "ZY"
# 
# 
#

# @lc code=start
class Solution:
    # 40ms, 62.68%; 13.7MB, 12.5%
    def convertToTitle(self, n: int) -> str:
        X=[]
        while n>0:
            if n%26!=0:
                X.insert(0,chr(n%26+64))
            else :
                X.insert(0,"Z")
            n=int((n-1)/26)
        return "".join(X)

# @lc code=end

