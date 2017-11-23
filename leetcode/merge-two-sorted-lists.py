# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
    def mergeTwoLists(self, l1, l2):
        
        arr=[];
        if None in (l1,l2):
            return l1 or l2
        else:
            while not (l1 == None):
                arr.append(l1.val)
                l1 = l1.next;
            while not (l2 == None):
                arr.append(l2.val);
                l2 = l2.next;

            return sorted(arr);
