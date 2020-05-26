#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#
# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (73.22%)
# Likes:    542
# Dislikes: 0
# Total Accepted:    177.8K
# Total Submissions: 242.8K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最大深度。
# 
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 返回它的最大深度 3 。
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
    # # 60ms, 34.54%; 15.5MB, 5.55%
    # # 递归:DFS
    # def maxDepth(self, root: TreeNode) -> int:
    #     return max(self.maxDepth(root.left)+1, self.maxDepth(root.right)+1) if root is not None else 0

    # 84ms, 6.08%; 14.9MB, 5.55%
    # 层次遍历：BFS
    def maxDepth(self, root: TreeNode) -> int:
        if root is None: return 0
        nodes = Queue()
        nodes.put(root)
        nodes.put(None)
        deep = 0
        while True:
            node = nodes.get()
            if node is None:
                deep += 1
                if nodes.empty(): return deep
                nodes.put(None)
            else:
                if node.left is not None:
                    nodes.put(node.left)
                if node.right is not None:
                    nodes.put(node.right)

# @lc code=end

