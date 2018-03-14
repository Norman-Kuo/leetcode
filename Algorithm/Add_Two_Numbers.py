#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        string1=""
        string2=""
        while l1:
            #print(l1.val)
            string1 = str(l1.val)+string1
            l1 = l1.next
        while l2:
            #print(l1.val)
            print(str(l2.val))
            string2 = str(l2.val)+string2
            l2 = l2.next
        sum = int(string1) + int(string2)
        answer = []
        for i in reversed(str(sum)):
            answer.append(int(i))
        return answer
