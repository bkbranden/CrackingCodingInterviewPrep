class ArrayList:
    def __init__(self):
        self.store = [None for _ in range(5)]
        self.size = 0
    
    def find(self, val):
        for i in self.store:
            if (val == self.store[i]):
                return self.store[i]
        return None

    def add(self, val):
        if (self.size >= len(self.store)):
            newArray = [None for _ in range(self.size*2)]
            for i in self.store:
                newArray[i] = self.store[i]
            self.store = newArray
        for i in range(0, len(self.store)):
            if self.store[i] == None:
                self.store[i] = val
                self.size+=1
                break


def main():
    ar = ArrayList()
    ar.add(2)
    ar.add(2)
    ar.add(2)
    ar.add(2)
    ar.add(2)
    ar.add(2)
    print(len(ar.store))


main()