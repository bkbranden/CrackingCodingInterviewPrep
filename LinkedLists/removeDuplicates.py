from util.linkedList import *


def removeDups(l):
    firstPointer = l.head.next
    secondPointer = l.head.next.next
    while(firstPointer != l.tail):
        while(secondPointer != l.tail):
            if(firstPointer.value == secondPointer.value):
                l.delete(firstPointer.value)
            secondPointer = secondPointer.next        
        firstPointer= firstPointer.next
        secondPointer = firstPointer.next
    
        
       
    return l


def main():
    
    lis = LinkedList()
    lis.appendToTail(1)
    lis.appendToTail(3)
    lis.appendToTail(8)
    lis.appendToTail(3)
    lis.appendToTail(4)
    lis.appendToTail(8)
    lis.appendToTail(91191)
    lis.appendToTail(3)
    lis.appendToTail(2)
    x = removeDups(lis)
    for i in x:
        print(i.value)




main()
