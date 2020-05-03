huffman code:
    optimal prefix code for compression

huffman encoding and decoding schema is lossless - no loss of information when compressing data 

assign codes for the relative frequency for each character e

huffman code can be any length 

this binary code can be visualized on a binary tree with each encoded character stored on leafs

Basic process:

1. build a Huffman tree

2. encode the data

3. decode the data

Pseudocode:

1. Determine relative frequencies of each character in a string: DONE

2. Build/sort a list of tuples from lowest to highest frequencies: DONE 

3. Build the Huffman Tree
    assign a binary code to each letter (shorter codes for more frequent letters)

    * implement a priority q using min heap

4. Trim the Huffman Tree
    remove the frequencies from the previous tree

5. Encode the text into compressed form 

6. Decode the text

Create encoding, decoding, sizing schemas

***

Relative Frequencies
    iterate through string
    each character is key
    value is count




