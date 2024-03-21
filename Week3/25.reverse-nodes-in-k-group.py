from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None

        new_head = None

        seg_start = head
        seg_end = head

        prev_seg_tail = None

        node_count = 1

        while seg_end is not None:
            next_head = seg_end.next
            if node_count % k == 0:
                # segment determined, reverse segment
                prev = None
                curr = seg_start

                while curr is not None and curr != next_head:
                    curr.next, prev, curr = prev, curr, curr.next

                if new_head is None:
                    new_head = seg_end

                if prev_seg_tail is not None:
                    prev_seg_tail.next = seg_end

                seg_start.next = next_head

                prev_seg_tail = seg_start

                seg_start = next_head

            seg_end = next_head
            node_count += 1

        return new_head
