import sys
from heapq import heappush, heappop, heapify


def huffman_encoding(data):

    # phase 1: build the Huffman Tree

    # compute frequency of each character
    frequencies = get_frequencies(data)

    # create a min-heap (binary tree: node <= child node)

    # first build a priority queue

    min_heap = []

    # priority queue
    for f in frequencies:
        freq = f[0]
        char = f[1]
        min_heap.append(Node(freq, char))

    # create a min-heap from priority queueue
    heapify(min_heap)

    # build the Huffman Tree from min-heap
    while len(min_heap) > 1:
        left_child = heappop(min_heap)
        right_child = heappop(min_heap)
        node = Node(left_child.freq + right_child.freq)
        node.left_child = left_child
        node.right_child = right_child
        heappush(min_heap, node)

    # phase 2: generate the encoded data

    # based on Huffman tree, generate unique binary code for each character in the string.
    root_node = heappop(min_heap)
    root_node_prefix = ''
    huffman_codes_map = generate_huffman_codes(root_node, root_node_prefix)

    # use huffman code map to complete huffman_code
    huffman_code = ''
    for c in data:
        huffman_code += huffman_codes_map[c]

    return huffman_code, root_node


def huffman_decoding(data, tree):
    current = tree
    decoded = ""

    for bit in data:
        if bit == '0':
            current = current.left_child
        else:
            current = current.right_child
        if current.left_child is None and current.right_child is None:
            decoded += current.char
            current = tree

    return decoded


def get_frequencies(data):
    freq_dict = dict()
    frequencies = []

    for c in data:
        if c in freq_dict:
            freq_dict[c] += 1
        else:
            freq_dict[c] = 1

    for key, value in freq_dict.items():
        frequencies.append((value, key))

    frequencies.sort(key=lambda x: x[0])

    return frequencies


def generate_huffman_codes(node, prefix):

    huffman_codes = {}

    def generate_codes(node, prefix=""):
        if node is None:
            return
        if node.right_child is None and node.left_child is None:
            huffman_codes[node.char] = prefix
        generate_codes(node.left_child, prefix + '0')
        generate_codes(node.right_child, prefix + '1')

    generate_codes(node)

    return huffman_codes


class Node:
    def __init__(self, freq, char=None):
        self.left_child = None
        self.right_child = None
        self.freq = freq
        self.char = char

    def __lt__(self, other):
        return self.freq < other.freq


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The content of the data is: {}\n".format(a_great_sentence))

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The content of the encoded data is: {}\n".format(encoded_data))

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The content of the decoded data is: {}\n".format(decoded_data))

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))

# Resources:
# https://www.studytonight.com/data-structures/huffman-coding
# https://www.cs.cmu.edu/~tcortina/15-121sp10/Unit06B.pdf
