"""
Preliminary notes:

Least Recently Used Cache

cache hit: for a get() operation, the entry is found in the cache 

cache miss: for a get() operation, the entry is not found in the cache

upper bound to size of the cache
    if cache is full, remove an element
    after removing an element, use put() operation to insert a new element

Design a data structure called Least Recently Used Cache

cache memory reaches it's limit, remove the least recently used cache

get() and set() operations are use() operation

choose a data structure to implement the cache

cache hit: get() returns the value
cache miss: get() returns -1

put element in the cache, put()/set() operation inserts the element

cache size is 5

if the cache is full, remove the least recently used cache and insert the element 

all operations must take O(1) time

"""

