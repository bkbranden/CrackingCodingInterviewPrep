class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.current = self.head
        self.head.next = self.tail

    def appendToTail(self, value):
        newNode = Node(value)
        if(self.head.next == self.tail):
            self.head.next = newNode
            self.current = newNode
            self.current.prev = self.head
            self.current.next = self.tail
            self.tail.prev = self.current
        else:
            while(self.current.next != self.tail):
                self.current = self.current.next
            self.current.next = newNode
            self.current.next.prev = self.current
            self.tail.prev = self.current.next
            self.current.next.next = self.tail

    def find(self, value):
        iterNode = self.head
        while(iterNode.next != self.tail):
            if(iterNode.value == value):
                return iterNode
            iterNode = iterNode.next
        return None

    def delete(self, value):
        iterNode = self.head
        while(iterNode.next != self.tail):
            if(iterNode.value == value):
                iterNode.next.prev = iterNode.prev
                iterNode.prev.next = iterNode.next
                break
            iterNode = iterNode.next
    

    def __iter__(self):
        self.currentIterator = self.head.next
        return self
    
    def __next__(self):
        if(self.currentIterator.next != None):
            node = self.currentIterator
            self.currentIterator = self.currentIterator.next
            return node
        raise StopIteration


class Node:
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.value = value

# def main():
#     lis = LinkedList()
#     lis.appendToTail(1)
#     lis.appendToTail(2)
#     lis.appendToTail(3)
#     lis.appendToTail(4)
#     lis.delete(3)

#     # x = lis.find(3)
#     # print(x.value)
#     for i in lis:
#         print(i.value)


# main()
