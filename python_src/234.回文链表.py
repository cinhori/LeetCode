#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#
# https://leetcode-cn.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (41.83%)
# Likes:    525
# Dislikes: 0
# Total Accepted:    96K
# Total Submissions: 227.9K
# Testcase Example:  '[1,2]'
#
# 请判断一个链表是否为回文链表。
# 
# 示例 1:
# 
# 输入: 1->2
# 输出: false
# 
# 示例 2:
# 
# 输入: 1->2->2->1
# 输出: true
# 
# 
# 进阶：
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # # 92ms, 38.92%; 24MB, 25%
    # def isPalindrome(self, head: ListNode) -> bool:
    #     stack = []
    #     while head:
    #         stack.append(head.val)
    #         head = head.next
    #     return stack == stack[::-1]

    # 72ms, 95.47%; 23.8MB, 25%
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next: return True
        pre, slow, fast = None, head, head.next
        while fast and fast.next:
            temp = slow.next
            slow.next = pre
            pre = slow
            slow = temp
            fast = fast.next.next
        
        if fast:
            fast = slow.next
            slow.next = pre
        else:
            fast = slow.next
            slow = pre
        while slow and fast:
            if fast.val != slow.val: return False
            fast, slow = fast.next, slow.next
        return not slow and not fast

# @lc code=end

