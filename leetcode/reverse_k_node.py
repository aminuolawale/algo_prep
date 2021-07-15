class Solution:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """"""
        leading_sentinel = ListNode()
        start = leading_sentinel
        start.next = head
        while True:
            counter = 1
            current_node = start.next
            if not current_node:
                break
            while counter < k:
                if current_node.next is None:
                    break
                current_node = current_node.next
                counter += 1
            trailer = current_node.next
            reversed_tail = self.reverseList(start.next, current_node)
            print(current_node)
            reversed_tail.next = trailer
            start = reversed_tail
        return leading_sentinel.next

    def reverseList(self, head, tail):
        if head.next == tail:
            tail.next = head
            head.next = None
            return head
        k = self.reverseList(head.next, tail)
        k.next = head
        return k.next
