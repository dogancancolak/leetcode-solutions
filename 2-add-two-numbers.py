# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode()
        sum_node = head
        carry = 0
        while l1 is not None or l2 is not None:
            first_val = l1.val if l1 is not None else 0
            second_val = l2.val if l2 is not None else 0
            sum = first_val+second_val
            if carry:
                sum = sum + carry
                carry = 0
            if sum >= 10:
                sum = sum % 10
                carry = 1
            sum_node.val = sum
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            if l1 is not None or l2 is not None:
                next = ListNode()
                sum_node.next = next
                sum_node = next
        if carry:
            last_node = ListNode(1)
            sum_node.next = last_node
        return head