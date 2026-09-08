class Node:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key -> Node
        self.head = Node() # dummy start
        self.tail = Node() # dummy end
        self.head.next = self.tail # start links
        self.tail.prev = self.head
    
    def _remove(self, node: Node):
        # take the node out of the list
        prev_node = node.prev 
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _append(self, node: Node):
        # add the node to the end of the list
        prev_tail = self.tail.prev # grab the real last node from the sentinel

        # append through
        prev_tail.next = node
        node.prev = prev_tail
        # update to link back to sentinel
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # grab the node from cache, remove, and append to its recent
        node = self.cache[key]
        self._remove(node)
        self._append(node)

        return node.value
        

    def put(self, key: int, value: int) -> None:
        # update node in cache
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            # refresh usage
            self._remove(node)
            self._append(node)
        else:
            # spawn a new node
            new = Node(key, value)
            # evict if needed
            if len(self.cache) >= self.capacity:
                lru_n = self.head.next
                self._remove(lru_n)
                del self.cache[lru_n.key]
            # add to cache with proper space already configured
            self.cache[key] = new
            self._append(new)
        
