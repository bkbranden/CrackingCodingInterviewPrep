from util.linkedList import *

def loopDetect(l):
    slowPointer = l.head.next
    fastPointer = l.head.next
    while(fastPointer.next != None):
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next.next
        if(slowPointer == fastPointer):
            break

    if(fastPointer == None or fastPointer.next == None):
        return None

    slowPointer = l.head.next
    while(slowPointer != fastPointer):
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next
    return fastPointer
    


def main():
    l1 = LinkedList()
    l1.appendToTail(3)
    l1.appendToTail(1)
    l1.appendToTail(5)
    l1.appendToTail(9)
    l1.appendToTail(7)
    l1.appendToTail(2)
    l1.appendToTail(1)
    # l1.appendToTail(7)
    l1.tail.prev.next = l1.head.next.next.next.next.next
    # for i in l1:
    #     print(i.value)

    x = loopDetect(l1)
    print(x)
    print(x.value)


main()