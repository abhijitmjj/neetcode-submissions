from typing import Optional, Dict

class Node:
    def __init__(self, key: Optional[int] = None, val: Optional[int] = None):
        self.key = key
        self.val = val
        self.prev: Optional["Node"] = None
        self.next: Optional["Node"] = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: Dict[int, Node] = {}   # key -> node

        # sentinels
        self.head = Node()   # MRU side
        self.tail = Node()   # LRU side
        self.head.next = self.tail
        self.tail.prev = self.head

    # ---- DLL helpers (all O(1)) ----
    def _remove(self, node: Node) -> None:
        p, n = node.prev, node.next
        p.next = n
        n.prev = p
        node.prev = node.next = None

    def _insert(self, node: Node) -> None:
        # insert right after head (MRU)
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _move_front(self, node: Node) -> None:
        self._remove(node)
        self._insert(node)

    def _pop_lru(self) -> Node:
        # node just before tail is LRU
        lru = self.tail.prev
        self._remove(lru)
        return lru

    # ---- API ----
    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if not node:
            return -1
        self._move_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._move_front(node)
            return

        # new key
        node = Node(key, value)
        self.cache[key] = node
        self._insert(node)

        # evict if over capacity (works even if capacity == 0)
        while len(self.cache) > self.capacity:
            victim = self._pop_lru()
            del self.cache[victim.key]
