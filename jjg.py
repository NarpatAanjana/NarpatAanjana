class Solution(object):
    def middleNode(self, head):
        end = head
        while end is not None and end.next is not None:
            head = head.next
            end = end.next.next
        return head
