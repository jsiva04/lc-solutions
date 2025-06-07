# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        elif not head.next:
            return False

        n1 = head
        n2 = head.next

        while True:
            try:
                n1 = n1.next
                n2 = n2.next.next

                if n2.next == n1:
                    return True
                if not n1.next or not n2.next:
                    return False
            except:
                return False