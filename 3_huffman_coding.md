## Explanation

### Discussion
To build the frequency map to track the frequency for each character,
I used a dictionary for fast insertion/lookup.

As a foundation for the Huffman Tree, I used a min heap which is a 
binary tree in which each node is less than or equal to the child nodes.

To build the min-heap I started by building a priority queue with nodes
storing the character and frequency.

### Time complexity

* Get the frequencies for each character by looping through each character, which takes O(n) time.

* We build the priority queue by looping through frequency list, which takes O(n) time.

* Building the min-heap using heapify takes O(n) time.
  https://www.growingwiththeweb.com/data-structures/binary-heap/build-heap-proof/

* To build the Huffman Tree from min-heap, we perform heappop and heappush operations which both take 
  take O(log(n)) time. We perform the operation for N items, so the result is O(n log n) time.
  https://www.cs.auckland.ac.nz/software/AlgAnim/huffman.html

* Decoding entails looping through the string of bits which takes O(n) time.

### Space complexity

* Creating the dictionary and list of tuples take O(n) space.

* Building the priority queue takes O(n) space.

* Building the min-heap using heapify takes O(n) space.

* The number of nodes used to building the Huffman Tree increases memory space on the order of O(n).

* We decode by constructing a string of characters, which takes O(n) space.
