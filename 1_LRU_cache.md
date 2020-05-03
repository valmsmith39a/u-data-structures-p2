## Explanation

### Discussion
In this exercise, there is a stipulation that all operations must take constant, O(1) time.
To satisfy this requirement, I used a dictionary to store/lookup key/value pairs in O(1) time.
I used a queue (enqueue/dequeue operations take O(1) time) to track the least recently used (LRU) item.
The head of the queue is the LRU item.

### Time complexity
Insert/lookup in a dictionary takes O(1) time.
Enqueue/dequeue operations on the queue take O(1) time.

### Space complexity
When a new item is added, we store the item in a dictionary and a queue.
So adding a new item takes 2*O(N) space, or simplified to O(N) space.

Getting an item does not take additional memory.
