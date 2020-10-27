# You are given two non-empty linked lists representing two non-negative integers.
#  The digits are stored in reverse order, and each of their nodes contains a single digit. 
#  Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def iteration(dataNode:ListNode):
    num = ''
    while dataNode is not None:
        num = num + str(dataNode.val)
        dataNode = dataNode.next
    return int(num)
def addition(l1:ListNode,l2:ListNode)->ListNode:
    carry = 0
    result = ListNode(0)
    result_tail = result
    while(l1 is not None or l2 is not None):
        value1 = (l1.val if l1 else 0)
        value2 = (l2.val if l2 else 0)
        carry, out = divmod(value1+value2 + carry, 10) 
        result_tail.next = ListNode(out)
        result_tail = result_tail.next
        l1 = (l1.next if l1 else None)
        l2 = (l2.next if l2 else None)
    return result.next
    

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return addition(l1,l2)

l1 = ListNode(2)
l12 = ListNode(4)
l13 = ListNode(3)
l12.next = l13
l1.next = l12

l2 = ListNode(5)
l22 =ListNode(8)
l33 = ListNode(4)
l23 = ListNode(3)

l22.next = l33
l33.next = l23
l2.next = l22
Solution().addTwoNumbers(l1,l2)