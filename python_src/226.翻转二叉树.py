#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#
# https://leetcode-cn.com/problems/invert-binary-tree/description/
#
# algorithms
# Easy (75.18%)
# Likes:    468
# Dislikes: 0
# Total Accepted:    86.5K
# Total Submissions: 114.8K
# Testcase Example:  '[4,2,7,1,3,6,9]'
#
# 翻转一棵二叉树。
# 
# 示例：
# 
# 输入：
# 
# ⁠    4
# ⁠  /   \
# ⁠ 2     7
# ⁠/ \   / \
# 1   3 6   9
# 
# 输出：
# 
# ⁠    4
# ⁠  /   \
# ⁠ 7     2
# ⁠/ \   / \
# 9   6 3   1
# 
# 备注:
# 这个问题是受到 Max Howell 的 原问题 启发的 ：
# 
# 谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。
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
    # # 32ms, 96.21%; 13.8MB, 5.26%
    # # 递归
    # def invertTree(self, root: TreeNode) -> TreeNode:
    #     if not root: return None
    #     temp = root.left
    #     root.left = root.right
    #     root.right = temp
    #     self.invertTree(root.left)
    #     self.invertTree(root.right)
    #     return root

    # # 40ms, 69.28%; 13.6MB, 5.26%
    # # 迭代
    # def invertTree(self, root: TreeNode) -> TreeNode:
    #     if not root: return None
    #     nodes = [root]
    #     while nodes:
    #         node = nodes.pop()
    #         if node.left: nodes.append(node.left)
    #         if node.right: nodes.append(node.right)
    #         temp = node.left
    #         node.left = node.right
    #         node.right = temp
    #     return root

    def invertTree(self, root: TreeNode) -> TreeNode:

# @lc code=end

