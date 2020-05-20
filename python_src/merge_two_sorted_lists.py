# 将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
# 示例：
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 48ms, 51.09%; 13.8MB, 7.14%
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    # 52ms, 30.48%; 13.7MB, 7.14%
    def mergeTwoLists2(self, l1, l2):
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
        prev.next = l1 if l1 is not None else l2
        return prehead.next


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next=ListNode(2)
    l1.next.next=ListNode(4)
    l2 = ListNode(1) 
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    res = Solution().mergeTwoLists2(l1, l2)
    while res is not None:
        print(res.val)
        res = res.next
    