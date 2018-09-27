from util.linkedList import *
import math

def partition(l, pivotValue):
    count = 0
    result = LinkedList()
    for i in l:
        count += 1
    ptr = l.head.next
    while(ptr != l.tail):
        if(ptr.value < pivotValue):
            result.appendToTail(ptr.value)
        ptr = ptr.next
    ptr = l.head.next
    while(ptr != l.tail):
        if(ptr.value >= pivotValue):
            result.appendToTail(ptr.value)
        ptr = ptr.next
    return result




def main():
    test = LinkedList()
    test.appendToTail(3)
    test.appendToTail(5)
    test.appendToTail(8)
    test.appendToTail(5)
    test.appendToTail(10)
    test.appendToTail(2)
    test.appendToTail(1)
    x = partition(test, 5)
    for i in x:
        print(i.value)



main()