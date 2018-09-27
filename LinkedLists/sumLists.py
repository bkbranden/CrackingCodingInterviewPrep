from util.linkedList import *

import math

def sumLists(l1, l2):
    multiplier1 = 1
    multiplier2 = 1
    runningSum1 = 0
    runningSum2 = 0
    ptr = l1.head.next
    ptr2 = l2.head.next
    while(ptr != l1.tail):
        runningSum1 += ptr.value * multiplier1
        multiplier1 *= 10
        ptr = ptr.next
    while(ptr2 != l2.tail):
        runningSum2 += ptr2.value * multiplier2
        multiplier2 *= 10
        ptr2 = ptr2.next
    result = runningSum1 + runningSum2
    return result

def sumLists2(l1, l2):
    len1 = -1
    len2 = -1
    for i in l1:
        len1+=1
    for i in l2:
        len2+=1    
    multiplier1 = math.pow(10,len1)
    
    multiplier2 = math.pow(10,len2)
    
    runningSum1 = 0
    runningSum2 = 0
    ptr = l1.head.next
    ptr2 = l2.head.next
    while(ptr != l1.tail):
        runningSum1 += ptr.value * multiplier1
        multiplier1 /= 10
        ptr = ptr.next
    while(ptr2 != l2.tail):
        runningSum2 += ptr2.value * multiplier2
        multiplier2 /= 10
        ptr2 = ptr2.next
    result = runningSum1 + runningSum2
    return result


def main():
    list1 = LinkedList()
    list2 = LinkedList()
    list1.appendToTail(6)
    list1.appendToTail(1)
    # list1.appendToTail(7)
    list2.appendToTail(2)
    list2.appendToTail(9)
    list2.appendToTail(5)
    x = sumLists2(list1, list2)
    print(int(x))


main()