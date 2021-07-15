#!usr/bin/python3
def printList(l):
    out = []
    while l is not None:
        out.append(l.val)
        l = l.next
    print(out)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = ListNode()
        current_node = head
        while l1 is not None or l2 is not None:
            if l1 is None:
                l1 = ListNode()
            if l2 is None:
                l2 = ListNode()
            current_sum = l1.val + l2.val + carry
            carry = current_sum // 10
            current_node.val = current_sum % 10
            if l1.next is not None or l2.next is not None:
                current_node.next = ListNode()
                current_node = current_node.next
            l1 = l1.next
            l2 = l2.next
        if carry:
            trailing_node = ListNode()
            trailing_node.val = carry
            current_node.next = trailing_node
        return head


list1 = ListNode()
list1.val = 2
a = ListNode()
a.val = 4
list1.next = a
b = ListNode()
b.val = 3
a.next = b

list2 = ListNode()
list2.val = 5
c = ListNode()
c.val = 6
list2.next = c
d = ListNode()
d.val = 4
c.next = d
printList(list1)
printList(list2)
printList(Solution().addTwoNumbers(list1, list2))
