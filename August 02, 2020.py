'''
705. Design HashSet

Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

add(value): Insert a value into the HashSet.
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

Example:

MyHashSet hashSet = new MyHashSet();
hashSet.add(1);
hashSet.add(2);
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);
hashSet.contains(2);    // returns true
hashSet.remove(2);
hashSet.contains(2);    // returns false (already removed)

Note:

All values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashSet library
'''
class ListNode:
    def __init__(self, val = None, nxt = None):
        self.val = val
        self.nxt = nxt
class MyHashSet:
    def __init__(self):
        self.size = 1000
        self.arr = [None] * self.size
    def hash(self, key):
        return key % self.size
    def find(self, key):
        position = self.hash(key)
        head = self.arr[position]
        while head:
            if head.val == key:
                return 1
            head = head.nxt
        return 0
    def add(self, key: int) -> None:
        if self.find(key): return
        position = self.hash(key)
        old_head = self.arr[position]
        head = ListNode(key, old_head)
        self.arr[position]=head
    def remove(self, key: int) -> None:
        position = self.hash(key)
        head = self.arr[position]
        if head is None: return
        if head.val == key:
            self.arr[position] = head.nxt
        pre, head = head, head.nxt
        while head:
            if head.val == key:
                pre.nxt = head.nxt
                return
            pre, head = head, head.nxt
    def contains(self, key: int) -> bool:
        return self.find(key)













