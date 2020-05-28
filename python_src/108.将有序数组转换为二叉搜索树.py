#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#
# https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/description/
#
# algorithms
# Easy (70.97%)
# Likes:    416
# Dislikes: 0
# Total Accepted:    68.4K
# Total Submissions: 96.4K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
# 
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
# 
# 示例:
# 
# 给定有序数组: [-10,-3,0,5,9],
# 
# 一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
# 
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
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
    # # 60ms, 62.41%; 15.8MB, 9.52%
    # # 中序遍历，选择中间位置左边元素为根节点
    # def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    #     def helper(left, right):
    #         if left > right:
    #             return None
    #         
    #         middle = (left + right) // 2
    #         root = TreeNode(nums[middle])
    #         root.left = helper(left, middle-1)
    #         root.right = helper(middle+1, right)
    #         return root

    #     return helper(0, len(nums)-1)

    # # 56ms, 79.46%; 16.1MB, 9.52%
    # # 中序遍历，选择中间位置右边元素为根节点
    # def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    #     def helper(left, right):
    #         if left > right:
    #             return None
            
    #         middle = (left + right) // 2
    #         if (left+right)%2: middle += 1
    #         root = TreeNode(nums[middle])
    #         root.left = helper(left, middle-1)
    #         root.right = helper(middle+1, right)
    #         return root

    #     return helper(0, len(nums)-1)

    # 60ms, 62.41%; 16MB, 9.52%
    # 中序遍历，随机选择中间位置左或右元素为根节点
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None
            
            middle = (left + right) // 2
            if (left+right)%2: middle += randint(0, 1)
            root = TreeNode(nums[middle])
            root.left = helper(left, middle-1)
            root.right = helper(middle+1, right)
            return root

        return helper(0, len(nums)-1)

# @lc code=end

