# https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.nodes = {}

        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_front(self, node):
        first = self.head.next

        self.head.next = node
        node.prev = self.head

        node.next = first
        first.prev = node

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1

        node = self.nodes[key]

        self._remove(node)
        self._insert_front(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            node = self.nodes[key]
            node.val = value

            self._remove(node)
            self._insert_front(node)
            return

        node = Node(key, value)

        self.nodes[key] = node
        self._insert_front(node)

        if len(self.nodes) > self.cap:
            lru = self.tail.prev

            self._remove(lru)
            del self.nodes[lru.key]
