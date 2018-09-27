class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self):
        self.storeValues = [None for _ in range(16)]
        self.size = 0
    
    def get(self, key):
        thiskeyhash = self.hash(key)
        thisposition = self.position(thiskeyhash)
        if not self.storeValues[thisposition]:
            return None
        else:
            list_at_index = self.storeValues[thisposition]
            for i in list_at_index:
                if i.key == key:
                    return i.value
            return None

            
    
    def put(self, key, value):
        puttingNode = Node(key, value)
        thiskeyhash = self.hash(key)
        thisposition = self.position(thiskeyhash)
        if not self.storeValues[thisposition]:
            self.storeValues[thisposition] = [puttingNode]
            self.size += 1 
        else:
            list_at_index = self.storeValues[thisposition]
            if puttingNode not in list_at_index:
                list_at_index[-1].next = puttingNode
                self.size += 1
            else:
                for i in list_at_index:
                    if i == puttingNode:
                        i.value = value
                        break





    def __len__(self):
        return self.size

    def hash(self, key):
        if isinstance(key, int):
            return key
        result = 5381
        for char in key:
            result = 33 * result + ord(char)
        return result
    
    def position(self, key_hash):
        return key_hash % 15

def main():
    hashmap = HashTable()
    hashmap.put(2, 12)
    hashmap.put('asd', 13)
    hashmap.put(2, 11)
    print(hashmap.get(2))
    print(hashmap.get('asd'))
    print(hashmap.get('ade'))

main()