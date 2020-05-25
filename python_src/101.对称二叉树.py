#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
# https://leetcode-cn.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (51.08%)
# Likes:    766
# Dislikes: 0
# Total Accepted:    137.7K
# Total Submissions: 269.6K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给定一个二叉树，检查它是否是镜像对称的。
# 
# 
# 
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
# 
# 
# 
# 
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
# 
# 
# 
# 
# 进阶：
# 
# 你可以运用递归和迭代两种方法解决这个问题吗？
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from queue import Queue

class Solution:
    #40ms, 84.76%; 13.8MB, 6.06%
    # 递归
    # def isSymmetric(self, root: TreeNode) -> bool:
    #     if root is None: return True
    #     return self._isSymmetric(root.left, root.right)

    # def _isSymmetric(self, left: TreeNode, right: TreeNode):
    #     if left is right: return True
    #     if (left and right) is None: return False
    #     if left.val == right.val:
    #         return self._isSymmetric(left.left, right.right) and self._isSymmetric(left.right, right.left)
    #     return False

    # 52ms, 29.96%; 14MB, 6.06%
    # def isSymmetric(self, root: TreeNode) -> bool:
    #     if root is None: return True
    #     left, right = Queue(), Queue()
    #     left.put(root.left)
    #     right.put(root.right)
    #     while not left.empty() and not right.empty():
    #         left_node = left.get()
    #         right_node = right.get()
    #         if left_node is right_node: continue
    #         if (left_node and right_node) is None: return False
    #         if left_node.val != right_node.val: return False
    #         else:
    #             left.put(left_node.left)
    #             left.put(left_node.right)
    #             right.put(right_node.right)
    #             right.put(right_node.left)
    #     return True

    # 60ms, 16.82%; 14MB, 6.06%;
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None: return True
        nodes = Queue()
        nodes.put(root.left)
        nodes.put(root.right)
        while not nodes.empty():
            left_node = nodes.get()
            right_node = nodes.get()
            if left_node is right_node: continue
            if (left_node and right_node) is None: return False
            if left_node.val != right_node.val: return False
            nodes.put(left_node.left)
            nodes.put(right_node.right)
            nodes.put(left_node.right)
            nodes.put(right_node.left)
        return True
             
# @lc code=end

