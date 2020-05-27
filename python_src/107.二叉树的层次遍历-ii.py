#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
#
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/description/
#
# algorithms
# Easy (65.51%)
# Likes:    237
# Dislikes: 0
# Total Accepted:    59.1K
# Total Submissions: 90.3K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
# 
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 返回其自底向上的层次遍历为：
# 
# [
# ⁠ [15,7],
# ⁠ [9,20],
# ⁠ [3]
# ]
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

from queue import Queue
class Solution:
    # # 56ms, 19.38%; 14.1MB, 6.25%
    # # bfs + queue
    # def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
    #     if root is None: return []
    #     nodes = Queue()
    #     nodes.put(root)
    #     nodes.put(None)
    #     nodes_lists = []
    #     nodes_list = []
    #     while True:
    #         node = nodes.get()
    #         if node is not None:
    #             nodes_list.append(node.val)
    #             if node.left is not None:
    #                 nodes.put(node.left)
    #             if node.right is not None:
    #                 nodes.put(node.right)
    #         else:
    #             nodes_lists.append(nodes_list)
    #             nodes_list = []
    #             if nodes.empty(): break
    #             nodes.put(None)
    #     nodes_lists.reverse()
    #     return nodes_lists

    # # bfs + queue   
    # # 44ms, 59.54%; 13.8MB, 6.25%
    # def levelOrderBottom(self, root):
    #     queue, res = collections.deque([(root, 0)]), []
    #     while queue:
    #         node, level = queue.popleft()
    #         if node:
    #             if len(res) < level+1:
    #                 res.insert(0, [])
    #             res[-(level+1)].append(node.val)
    #             queue.append((node.left, level+1))
    #             queue.append((node.right, level+1))
    #     return res    

    # dfs + stack
    # 40ms, 79.74%; 14.1MB, 6.25%
    def levelOrderBottom(self, root):
        stack, res = [(root, 0)], []
        while stack:
            node, level = stack.pop()
            if node:
                if len(res) < level+1:
                    res.insert(0, [])
                res[-(level+1)].append(node.val)
                stack.append((node.right, level+1))
                stack.append((node.left, level+1))
        return res

# @lc code=end

