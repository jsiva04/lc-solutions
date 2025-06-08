# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        if not head.next.next:
            if n == 1:
                head.next = None
                return head
            elif n == 2:
                return head.next
        
        list1 = head
        list2 = head

        for i in range(n):
            list2 = list2.next
        
        if list2 == None:
            return head.next

        while list2.next:
            list1 = list1.next
            list2 = list2.next
        
        print(list1.val)
        print(list2.val)

        list1.next = list1.next.next

        return head