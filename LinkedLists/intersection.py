from util.linkedList import *

def intersection(l1, l2):
    len1 = 0
    len2 = 0
    for i in l1:
        len1 += 1
    for j in l2:
        len2 += 1
    combinedLength = abs(len1 - len2)
    count = 0
    ptr1 = l1.head.next
    while(count < combinedLength):
        count += 1
        ptr1 = ptr1.next
    ptr2 = l2.head.next
    while(ptr1 != l1.tail and ptr2 != l2.tail):
        if(ptr1 == ptr2):
            return ptr1
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    return None



def main():
    l1 = LinkedList()
    l1.appendToTail(3)
    l1.appendToTail(1)
    l1.appendToTail(5)
    l1.appendToTail(9)
    l1.appendToTail(7)
    l1.appendToTail(2)
    l1.appendToTail(1)

    l2 = LinkedList()
    l2.appendToTail(4)
    l2.appendToTail(6)
    linkingNode = l1.find(7)
    linkingNode.prev = l2.tail.prev
    linkingNode.next = l2.tail
    l2.tail.prev.next = linkingNode
    l2.appendToTail(2)
    l2.appendToTail(1)

    x = intersection(l1,l2)
    print(x)
    print(x.value)



main()