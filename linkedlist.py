from ListNode import ListNode
import copy 

def main():
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    a.next.next.next.next = ListNode(5)
    removeNthFromEnd(a, 2)
    # deleteNode(a.next.next)



def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next



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