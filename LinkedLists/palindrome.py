from util.linkedList import *

def palin(l):
    startPointer = l.head.next
    endPointer = l.tail.prev
    while(startPointer != endPointer):
        if(startPointer.value != endPointer.value):
            return False
        else:
            startPointer = startPointer.next
            endPointer = endPointer.prev
    
    return True



def main():
    l = LinkedList()
    l.appendToTail(0)
    l.appendToTail(1)
    l.appendToTail(2)
    l.appendToTail(1203)
    l.appendToTail(2)
    l.appendToTail(1)
    l.appendToTail(0)
    print(palin(l))


main()