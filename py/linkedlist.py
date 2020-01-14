from ListNode import ListNode
import copy 

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def main():
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    a.next.next.next.next = ListNode(5)
    # removeNthFromEnd(a, 2)
    # deleteNode(a.next.next)
    iteratelinkedList(a)
    reverseLL(a)

def iteratelinkedList(node: ListNode):
    print('iterate list')
    while node.next:
        print(node.val)
        node = node.next
    if node: print(node.val)


def deleteNode(node: ListNode):
    node.val = node.next.val
    node.next = node.next.next

def reverseLL(node: ListNode) -> ListNode:
    prev = None
    while node:
        curr = node
        node = node.next
        curr.next = prev
        prev = curr
    return prev

def mergeList(l1: ListNode, l2: ListNode):
    dummy = cur = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next

def isPalindrome(self, head: ListNode) -> bool:
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    return vals == vals[::-1]



def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    length  = 0
    first = head
    while first != None:
        length+=1
        first = first.next
    print(length)
    length -= n
    print(length)
    first = dummy
    while length > 0:
        length-=1
        first = first.next
    first.next = first.next.next
    print(dummy.next.val)
    return dummy.next                

if __name__ == "__main__":
    main()