#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#
# https://leetcode-cn.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (63.85%)
# Likes:    274
# Dislikes: 0
# Total Accepted:    41.1K
# Total Submissions: 64.1K
# Testcase Example:  '[1,2,3,null,5]'
#
# 给定一个二叉树，返回所有从根节点到叶子节点的路径。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例:
# 
# 输入:
# 
# ⁠  1
# ⁠/   \
# 2     3
# ⁠\
# ⁠ 5
# 
# 输出: ["1->2->5", "1->3"]
# 
# 解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
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
    # # 40ms, 79.33%; 13.8MB, 7.14%
    # def binaryTreePaths(self, root: TreeNode) -> List[str]:
    #     if not root: return []
    #     result = []
    #     def _binaryTreePaths(now_path, node):
    #         if node.left == node.right:
    #             result.append(now_path)
    #             return
    #         if node.left:
    #             _binaryTreePaths(now_path+'->'+str(node.left.val), node.left)
    #         if node.right:
    #             _binaryTreePaths(now_path+'->'+str(node.right.val), node.right)
        
    #     _binaryTreePaths(str(root.val), root)
    #     return result

    # 44ms, 56.9%; 13.8MB, 7.14%
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return []
        result, stack = [], [(root, str(root.val))]
        while stack:
            node, path = stack.pop()
            if node.left == node.right:
                result.append(path)
                continue
            if node.right:
                stack.append((node.right, path+'->'+str(node.right.val)))
            if node.left:
                stack.append((node.left, path+'->'+str(node.left.val)))
        return result


# @lc code=end

