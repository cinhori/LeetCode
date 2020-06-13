#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#
# https://leetcode-cn.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (45.43%)
# Likes:    397
# Dislikes: 0
# Total Accepted:    82.5K
# Total Submissions: 180.8K
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# 删除链表中等于给定值 val 的所有节点。
# 
# 示例:
# 
# 输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 哨兵
    # 92ms, 24.6%; 16.6MB, 11.11%
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        pre_head = ListNode(1)
        pre_head.next = head
        pre, now = pre_head, head
        while now:
            if now.val == val:
                pre.next = now.next
                now = now.next
            else:
                pre = now
                now = now.next
        return pre_head.next

# @lc code=end

