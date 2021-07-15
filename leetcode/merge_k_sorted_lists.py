class Solution:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # put  code here
        if not lists:
            return None
        if len(lists) == 1 and lists[0] == []:
            return None
        result = ListNode()
        running = result
        while True:
            current_node, index = self.get_minimum_node(lists)
            if current_node is None:
                return result.next
            running.next = current_node
            running = running.next
            lists[index] = lists[index].next
        return result.next

    def get_minimum_node(self, lists):
        min_node = lists[0]
        index = 0
        ind = 0
        while index < len(lists):
            if not min_node or (lists[index] and lists[index].val < min_node.val):
                min_node = lists[index]
                ind = index
            index += 1
        return min_node, ind
