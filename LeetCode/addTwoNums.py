# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # create a new LL
        carry = 0
        l3 = ListNode()
        cur = l3
        # traverse the lists
        while l1 or l2 or carry:
            # add the carry to sum if it exists
            sum = 0
            sum = sum + carry
            carry = 0
            # add the first value to sum
            # then move to the next node
            if l1:
                sum += l1.val
                l1 = l1.next
            # repeat for l2
            if l2:
                sum += l2.val
                l2 = l2.next
            # check if the number is over 10
            if sum >= 10:
                sum = sum - 10
            # if it is add 1 to carry (and then 1 to the next int)
                carry = carry + 1
            # add sum to l3
            cur.next = ListNode(sum)
            cur = cur.next
        return l3.next
