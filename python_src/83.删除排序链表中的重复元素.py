#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (50.36%)
# Likes:    310
# Dislikes: 0
# Total Accepted:    101.2K
# Total Submissions: 200.9K
# Testcase Example:  '[1,1,2]'
#
# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
# 
# 示例 1:
# 
# 输入: 1->1->2
# 输出: 1->2
# 
# 
# 示例 2:
# 
# 输入: 1->1->2->3->3
# 输出: 1->2->3
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 44ms, 89.86%; 6.06%, 13.7MB
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next == None: return head
        last = head
        pointer = head.next
        while pointer is not None:
            if pointer.val == last.val: pointer = pointer.next
            elif last.next == pointer: 
                last = pointer
                pointer = pointer.next
            else:
                last.next = pointer
                last = pointer
                pointer = pointer.next

        last.next = None
        return head

# @lc code=end
        
