## Explanation

### Discussion

To create a blockchain, we use a linked list data structure to store 
a timestamp, user-defined data, a reference to the next block and 
the hash value of the previous block. A linked list was used because it 
satisfies the specifications of a blockchain.

### Time Complexity

Appending a new block to the blockchain takes O(N) time because
we need to traverse all the blocks before inserting the block at the 
end of the chain.

### Space Complexity

Appending a new block to a blockhain takes O(1) or constant space.
No matter how big the chain, we only add 1 block at a time and the 
amount of memory we consume to traverse the list does not increase
with the size of the chain.
