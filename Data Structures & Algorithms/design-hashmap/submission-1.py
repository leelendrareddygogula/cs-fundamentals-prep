class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.my_map = [Node(0,0) for i in range(1000)] 

    def put(self, key: int, value: int) -> None:
        index = key % 1000
        current = self.my_map[index]
        while(current.next):
            if(current.next.key == key):
                current.next.value = value
                return
            current = current.next
        current.next = Node(key, value)
        

    def get(self, key: int) -> int:
        index = key % 1000
        current = self.my_map[index]
        while(current.next):
            if(current.next.key == key):
                return current.next.value
            current = current.next
        return -1

    def remove(self, key: int) -> None:
        index = key % 1000
        current = self.my_map[index]
        while(current.next):
            if(current.next.key == key):
               current.next = current.next.next 
               return
        return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)