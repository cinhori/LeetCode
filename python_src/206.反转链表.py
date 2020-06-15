#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
# https://leetcode-cn.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (69.07%)
# Likes:    1008
# Dislikes: 0
# Total Accepted:    255.1K
# Total Submissions: 367.9K
# Testcase Example:  '[1,2,3,4,5]'
#
# 反转一个单链表。
# 
# 示例:
# 
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
# 
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # # 52ms, 31.37%; 19.9MB, 5.88%
    # # 递归
    # def reverseList(self, head: ListNode) -> ListNode:
    #     self.real_head = None
    #     def _reverseListHelper(head):
    #         if not head or not head.next:
    #             self.real_head = head
    #             return head
    #         else:
    #             last = _reverseListHelper(head.next)
    #             last.next = head
    #             head.next = None
    #             return head

    #     _reverseListHelper(head)
    #     return self.real_head

    # 44ms, 73.14%; 18.6MB, 5.88%
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last

    # # 48ms, 52.15%; 14.7MB, 17.65%;
    # def reverseList(self, head: ListNode) -> ListNode:
    #     if not head or not head.next: return head
    #     first, second, third = head, head.next, head.next.next
    #     first.next = None
    #     while True:
    #         second.next = first
    #         if not third:
    #             return second
    #         else:
    #             first, second, third = second, third, third.next

    # # 48ms, 52.15%; 14.6MB, 17.65%;
    # def reverseList(self, head: ListNode) -> ListNode:
    #     pre, current = None, head
    #     while current:
    #         temp = current.next
    #         current.next = pre
    #         pre = current
    #         current = temp
    #     return pre
            
# @lc code=end

