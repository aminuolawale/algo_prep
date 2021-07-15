class Solution:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

        def __eq__(self, a, b):
            return a.val == b.val and a.next == b.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        result = ListNode()
        for l in lists:
            result = self.merge(result, l)
        return result.next

    def merge(self, a, b):
        result = ListNode()
        curr = result
        while a is not None and b is not None:
            the_min, the_max = self.min_node(a, b)
            curr.next = the_min
            curr = curr.next
            a = the_min.next
            b = the_max
        return result.next

    def min_node(self, a, b):
        if not b:
            return a
        if not a:
            return b
        return a, b if a.val < b.val else b, a
