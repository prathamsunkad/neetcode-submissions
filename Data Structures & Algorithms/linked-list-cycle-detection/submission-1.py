# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        speed1 = head;
        speed2 = head;

        if(head is None):
            return False

        if(head.next is None):
            return False


        while True:
            speed1 = speed1.next
            if(speed2.next is None):
                return False
                break
                
            speed2 = speed2.next.next

            if speed2 is None:
                return False
                break

            if speed1 == speed2:
                break
        return True

            
        