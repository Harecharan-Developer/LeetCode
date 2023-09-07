# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        x = head
        divider_corrector = 0

        while x:
            length += 1
            x = x.next

        divider = [length // k] * k

        for i in range(length % k):
            divider[i] += 1

        output = []
        current = head

        for part_size in divider:
            if part_size == 0:
                output.append(None)
            else:
                output.append(current)
                for _ in range(part_size - 1):
                    current = current.next
                temp = current.next
                current.next = None
                current = temp

        return output
