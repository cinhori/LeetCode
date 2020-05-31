#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#
# https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (42.42%)
# Likes:    258
# Dislikes: 0
# Total Accepted:    77.3K
# Total Submissions: 182.1K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最小深度。
# 
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例:
# 
# 给定二叉树 [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 返回它的最小深度  2.
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
    # # 52ms, 84.15%; 15.7MB, 12.5%
    # def minDepth(self, root: TreeNode) -> int:
    #     if not root: return 0
    #     if root.left is root.right: return 1
    #     if (not root.left) and root.right: return self.minDepth(root.right)+1
    #     if root.left and (not root.right): return self.minDepth(root.left)+1
    #     return min(self.minDepth(root.left)+1, self.minDepth(root.right)+1)

    # # 60ms, 47.92%; 14.8MB, 12.5%
    # def minDepth(self, root: TreeNode) -> int:
    #     if root is None: return 0
    #     stack = [(root, 1)]
    #     min_deep = sys.maxsize
    #     while len(stack):
    #         node, deep = stack.pop()
    #         if node.left is node.right:
    #             min_deep = min_deep if min_deep < deep else deep
    #             continue
    #         if node.left: stack.append((node.left, deep+1))
    #         if node.right: stack.append((node.right, deep+1))
    #     return min_deep

    # 100ms, 5.71%; 14.9MB, 12.5%
    def minDepth(self, root: TreeNode) -> int:
        if root is None: return 0
        node_queue = Queue()
        node_queue.put((root, 1))
        min_deep = sys.maxsize
        while not node_queue.empty():
            node, deep = node_queue.get()
            if node.left is node.right:
                min_deep = min_deep if min_deep < deep else deep
                continue
            if node.left: node_queue.put((node.left, deep+1))
            if node.right: node_queue.put((node.right, deep+1))
        return min_deep

# @lc code=end

