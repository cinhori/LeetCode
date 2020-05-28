#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#
# https://leetcode-cn.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (51.75%)
# Likes:    322
# Dislikes: 0
# Total Accepted:    76.7K
# Total Submissions: 148.2K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，判断它是否是高度平衡的二叉树。
# 
# 本题中，一棵高度平衡二叉树定义为：
# 
# 
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
# 
# 
# 示例 1:
# 
# 给定二叉树 [3,9,20,null,null,15,7]
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 返回 true 。
# 
# 示例 2:
# 
# 给定二叉树 [1,2,2,3,3,null,null,4,4]
# 
# ⁠      1
# ⁠     / \
# ⁠    2   2
# ⁠   / \
# ⁠  3   3
# ⁠ / \
# ⁠4   4
# 
# 
# 返回 false 。
# 
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
    # # 92ms, 20.6%; 18.4MB, 7.69%;
    # # 自顶向下，getHeight存在大量冗余
    # def isBalanced(self, root: TreeNode) -> bool:
    #     def getHeight(node):
    #         if node is None: return 0
    #         else: return max(getHeight(node.left)+1, getHeight(node.right)+1)

    #     if root is None: return True
    #     if abs(getHeight(root.left)-getHeight(root.right)) > 1: return False
    #     else: return self.isBalanced(root.left) and self.isBalanced(root.right)

    # # Return whether or not the tree at root is balanced while also returning
    # # the tree's height
    # 自底向上的递归
    # # 60ms, 83,53%; 17.7MB, 7.69%;
    # def isBalancedHelper(self, root: TreeNode) -> (bool, int):
    #     # An empty tree is balanced and has height -1
    #     if not root:
    #         return True, -1
        
    #     # Check subtrees to see if they are balanced. 
    #     leftIsBalanced, leftHeight = self.isBalancedHelper(root.left)
    #     if not leftIsBalanced:
    #         return False, 0
    #     rightIsBalanced, rightHeight = self.isBalancedHelper(root.right)
    #     if not rightIsBalanced:
    #         return False, 0
        
    #     # If the subtrees are balanced, check if the current tree is balanced
    #     # using their height
    #     return (abs(leftHeight - rightHeight) < 2), 1 + max(leftHeight, rightHeight)
        
    # def isBalanced(self, root: TreeNode) -> bool:
    #     return self.isBalancedHelper(root)[0]

    # 60ms, 83,53%; 18.5MB, 7.69%;
    def isBalanced(self, root: TreeNode) -> (bool, int):
        def helper(node):
            if node is None: return 0

            left, right = helper(node.left), helper(node.right)
            if left == -1 or right == -1 or abs(left-right) > 1:
                return -1
            return max(left, right) + 1

        return helper(root) >= 0
        
# @lc code=end

