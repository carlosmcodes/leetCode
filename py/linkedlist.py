from ListNode import ListNode
import copy 

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def main():
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(5)
    b = ListNode(3)
    b.next = ListNode(1)
    b.next.next = ListNode(2)
    b.next.next.next = ListNode(5)
    # a.next.next.next = ListNode(4)
    # a.next.next.next.next = ListNode(5)
    # a.next.next.next.next.next = ListNode(3)
    ilist = []
    # for i in range(5):
    #     ilist.append(ListNode(i))
    # # removeNthFromEnd(a, 2)
    # # deleteNode(a.next.next)
    # iteratelinkedList(a)
    # reverseLL(a)
    # removeDupsLinkedList(a)
    # for i in range(6):
    # kth2last(3, a)
    # iteratelinkedList(a)
    # print(sumList(a,0))
    # print(sum2List(a, b))
    # printLL(a)
    # printLL(b)
    # isPali_onlyLL(a)
    # printLL(a)
    # printLL(createRev_LL_recursively(a))
    # print(isPali_onlyLL(a))
    # print(LL_intersect(a, b))
    a = ll_intersect_onlyLL(a,b)
    print(a)
def ll_intersect_onlyLL(a: ListNode, b: ListNode):
    reva = reverseLL(a)
    revb = reverseLL(b)
    lena = length(reva)
    lenb = length(revb)
    shorter = lena if lena < lenb else lenb
    for i in range(shorter):
        if reva.val != revb.val: 
            return reva
        reva = reva.next
        revb = revb.next
    return None


def LL_intersect(a: ListNode, b: ListNode):
    dicto = {}
    if not a or not b: return 0
    while a: 
        if a.val not in dicto:
            dicto[a.val] = 0
        a = a.next
    while b: 
        if b.val in dicto:
            dicto[b.val] = dicto.get(b.val,0) + 1
        b = b.next
    purge = [value for value,key in enumerate(dicto) if value >=1]
    return purge
"""
returns T/F if linked list is palindrone. using ONLY linkedlist pointers
"""
def isPali_onlyLL(head: ListNode):
    temp_copy = createReversedList(head)
    while head.next:
        if head.val != temp_copy.val: return False
        head = head.next
        temp_copy = temp_copy.next
    return True

"""
this creates a new LinkedList recursively :)
"""
def createRev_LL_recursively(node: ListNode, head=None):
    if not node: return head
    temp = ListNode(node.val)
    temp.next = head
    head = temp
    return createRev_LL_recursively(node.next, head)

"""
creates a new linked list iteratively
"""
def createReversedList(node: ListNode):
    head = ListNode(None)
    while node:
        temp = ListNode(node.val)
        temp.next = head
        head = temp
        node = node.next
    return head

def sum2List(a: ListNode, b: ListNode, val=0 , power=0):
    alen = length(a)
    blen = length(b)
    print(f'alen, blen: {alen}, {blen}')
    longest = alen if alen > blen else blen
    print(f'longest : {longest}')
    if not a and not b: return val
    if not a:
        return sum2List(None, b.next, val + b.val * pow(10, power), power+1)
    if not b: 
        return sum2List(a.next, None, val + a.val * pow(10, power), power+1)
    print(val)
    return sum2List(a.next, b.next, val + (a.val + b.val)  * pow(10 , power), power+1)    

""" 
iterate list  and add elements recursively
"""
def sumList(head: ListNode, val: int):
    if not head: return val
    return sumList(head.next, val + head.val)


def length(a: ListNode)-> int:
    count = 0
    copy = a
    while copy:
        copy = copy.next
        count +=1
    return count
def removeDupsLinkedList(head) -> ListNode: 
    dicto = []
    copy = head
    return dups_helper(head, dicto)
    # return copy

def kth2last(kth: int, head: ListNode) -> ListNode:
    if not head: return None
    dummy = head
    count = 0
    getk = head
    while dummy:
        dummy = dummy.next
        count+=1
    k = count - kth
    for i in range(k):
        getk = getk.next
    print(getk.val)
    return getk


def dups_helper(head: ListNode, dicto): 
    if not head: return 
    if head.val in dicto:
        deleteNode(head)
    else:
        dicto.append(head.val)
    # print(f"head.val {head.val}")
    return dups_helper(head.next, dicto)

def iteratelinkedList(node: ListNode):
    print('iterate list')
    while node.next:
        print(node.val)
        node = node.next
    if node: print(node.val)


def deleteNode(node: ListNode):
    node.val = node.next.val
    node.next = node.next.next

"""
in place reversing
"""
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

def printLL(node: ListNode): 
    while node.next:
        print(f'{node.val} ->', end=" ")
        node = node.next
    print(node.val)  

if __name__ == "__main__":
    main()