class LRU_Cache(object):
    """
    Least Recently Used Cache
        * Implement a cache that stores up to 5 items.
        * If the cache is full, remove the least recently used (LRU) item and
          store the new item.
        * All operations must take O(1) (constant) time.

    Attributes:
        cache (dictionary): stores the key and value
        head (class: Node): tracks head of list
        tail (class: Node): tracks tail of list
        size (int): current size of the cache
        capacity (int): max size of the cache
    """

    def __init__(self, capacity):
        # Initialize class variables
        self.cache = dict()
        self.head = None
        self.tail = None
        self.size = 0
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cache:
            node = self.cache[key]
            return node.value
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        node = LinkedListNode(key, value)

        if self.size == self.capacity:
            if self.head is None:
                return
            # get the lru key
            lru_key = self.head.key

            # remove the lru item from cache
            del self.cache[lru_key]

            # dequeue the lru item
            self.head = self.head.next

            # insert new item into cache
            self.cache[key] = node

            # enqueue the new item in queue
            if self.head is None:
                self.head = node
                self.tail = self.head
            else:
                self.tail.next = node
                self.tail = self.tail.next

        else:
            # Prevent negative cache capacity values
            if self.capacity < 0:
                return
            # enqueue new item
            if self.head is None:
                self.head = node
                self.tail = self.head
            else:
                self.tail.next = node
                self.tail = self.tail.next

            # insert new item into cache
            self.cache[key] = node
            self.size += 1

    def get_size(self):
        return self.size


class LinkedListNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


our_cache = LRU_Cache(5)

# Test 1a

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)

print("--- Test 1a ---")
print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(3))  # returns 3

# Test 1b

print("--- Test 1b ---")
print(our_cache.get(23))  # returns -1 because 23 does not exist

# Test 1c

our_cache.set(4, 4)
our_cache.set(5, 5)
our_cache.set(6, 6)
print("--- Test 1c ---")
print(our_cache.get_size())  # returns 5
print(our_cache.get(6))      # returns 6
print(our_cache.get(1))      # returns -1 because 1 has been replaced by 6

# Test 2
print("--- Test 2 ---")
our_cache_2 = LRU_Cache(0)
our_cache_2.set(1, 1)
print(our_cache_2.get(1))    # returns -1

# Test 3
print("--- Test 3 ---")
our_cache_3 = LRU_Cache(-1)
our_cache_3.set(1, 1)
print(our_cache_3.get(1))   # returns -1
