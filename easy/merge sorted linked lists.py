#uses recursion
#beats 100% submissions
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1 or not list2:
          return list1.val or list2.val
        if list1.val<list2.val:
          list1.next = self.mergeTwoLists(list1.next,list2)
          return list1.val
        else:
          list2.next = self.mergeTwoLists(list1,list2.next)
          return list2.val
if __name__ == "__main__":
  list1 = ListNode(1,ListNode(2,ListNode(4)))
  list2 = ListNode(1,ListNode(3,ListNode(4)))




  sol = Solution()
  res = sol.mergeTwoLists(list1, list2)
  print(res)