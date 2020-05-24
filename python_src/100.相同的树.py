#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#
# https://leetcode-cn.com/problems/same-tree/description/
#
# algorithms
# Easy (57.66%)
# Likes:    365
# Dislikes: 0
# Total Accepted:    88.3K
# Total Submissions: 153.2K
# Testcase Example:  '[1,2,3]\n[1,2,3]'
#
# 给定两个二叉树，编写一个函数来检验它们是否相同。
# 
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
# 
# 示例 1:
# 
# 输入:       1         1
# ⁠         / \       / \
# ⁠        2   3     2   3
# 
# ⁠       [1,2,3],   [1,2,3]
# 
# 输出: true
# 
# 示例 2:
# 
# 输入:      1          1
# ⁠         /           \
# ⁠        2             2
# 
# ⁠       [1,2],     [1,null,2]
# 
# 输出: false
# 
# 
# 示例 3:
# 
# 输入:       1         1
# ⁠         / \       / \
# ⁠        2   1     1   2
# 
# ⁠       [1,2,1],   [1,1,2]
# 
# 输出: false
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 28ms, 98.45%; 13.4MB, 7.14%;
    # 递归
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None: return True
        elif p is None or q is None or p.val != q.val: return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    # 迭代：广度遍历，使用队列
# @lc code=end

