from util.linkedList import *

def kth(l, value):
    # newList = LinkedList()
    count = 0
    ptr = l.head.next
    while(ptr != l.tail):
        count+=1
        ptr = ptr.next
    newCount = count -value
    count = 0
    ptr = l.head.next
    while(count < newCount):
        count += 1
        ptr = ptr.next
    # while(ptr != l.tail):
    #     newList.appendToTail(ptr.value)
    #     ptr = ptr.next
    # return newList
    return ptr.value



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
    x = kth(lis, 8)
    print(x)
    # for i in x:
    #     print(i.value)


main()