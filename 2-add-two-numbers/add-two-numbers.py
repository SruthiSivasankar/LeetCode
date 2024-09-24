class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    #NOTHING CAN BE CHANGED BELOW
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode')->'ListNode':
        show = False
        assert_answers = True
        ans = [None] #List of size 1
        h = L0002(l1,l2,ans,assert_answers,show)
        return ans[0]

class L0002:
    def __init__(self, l1: 'ListNode', l2: 'ListNode', ans:'listNode of size 1', assert_answers:'bool',show:'bool') -> None:
        #NOTHING CAN BE CHANGED BELOW
        self._a = Slist()
        self._a._first = l1
        self._b = Slist()
        self._b._first = l2
        self._ans = ans
        self._alg()
        
    def _alg(self):
        c = self._a + self._b
        self._ans[0] = c._first


class Slist():
    def __init__(self):
        #NOTHING CAN BE CHANGED HERE
        self._first = None
        self._last = None

    #############################
    # WRITE CODE BELOW
    #############################

    def __add__(self, other):
        result = Slist()
        carry = 0
        p1 = self._first
        p2 = other._first

        while p1 or p2 or carry:
            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            result.append(digit)

            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next

        return result



    def append(self, val):
            new_node = ListNode(val)

            if not self._first:
                self._first = new_node
                self._last = new_node
            else:
                self._last.next = new_node
                self._last = new_node