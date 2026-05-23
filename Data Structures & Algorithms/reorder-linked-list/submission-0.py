# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:


        if not head.next or not head.next.next:
            return

        # Find middle
        speed1 = head
        speed2 = head

        while speed2.next and speed2.next.next:
            speed1 = speed1.next
            speed2 = speed2.next.next

        secondhalf = speed1.next
        speed1.next = None

        # Reverse second half
        front = secondhalf.next
        current = secondhalf
        current.next = None  # ✅ prevent cycle

        while front:
            p = front.next
            front.next = current
            current = front
            front = p

        # Merge two halves
        current1 = head
        current2 = current

        while current1 and current2:
            front1 = current1.next
            front2 = current2.next

            current1.next = current2
            if not front1:
                break
            current2.next = front1

            current1 = front1
            current2 = front2