import sys
from heapq import heappush, heappop, heapify


def huffman_encoding(data):
    """
    Data compression by Huffman coding algorithm.

    Parameters:
        data (str): string data to encode

    Returns:
        huffman_code (str): encoded string of bits
        root_node (class: Node): root node of Huffman Tree
    """

    if data == "" or data is None:
        return None, None

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
    """
    Decode Huffman code

    Parameters:
        data (str): string of bits

    Returns:
        decoded (str): decoded data in original form
    """
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
    """
    Get frequencies for each character.

    Parameters:
        data (str): data string

    Returns:
        frequencies (list): list of tuples containing frequency and character
    """
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
    """
    Generate Huffman codes for each character by traversing the tree
    and assigning '0' to a move towards left child node and '1' to right child node.

    Parameters:
        node (class: Node): root node of Huffman Tree
        prefix (str): starting prefix
    Returns:
        huffman_codes (dictionary): map of characters to generated Huffman codes
    """

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
    """
    Create a node used to build a tree.

    Attributes:
        left_child (class: Node): left child of a node
        right_child (class: Node): right child of a node
        freq: frequency of a character
        char: character
    """

    def __init__(self, freq, char=None):
        self.left_child = None
        self.right_child = None
        self.freq = freq
        self.char = char

    def __lt__(self, other):
        return self.freq < other.freq


def print_test_results(input_data):
    encoded_data = ""
    decoded_data = ""

    print("The content of the data is: {}\n".format(input_data))

    print("The size of the data is: {}\n".format(
        sys.getsizeof(input_data)))

    if len(get_frequencies(input_data)) == 1:

        encoded_data = len(input_data) * '0'

        print("The content of the encoded data is: {}\n".format(encoded_data))

        print("The size of the encoded data is: {}\n".format(
            sys.getsizeof(int(encoded_data, base=2))))

        decoded_data = input_data

        print("The content of the decoded data is: {}\n".format(decoded_data))

        print("The size of the decoded data is: {}\n".format(
            sys.getsizeof(decoded_data)))
        return

    else:
        encoded_data, tree = huffman_encoding(input_data)

    if encoded_data is None:
        print("No input data")
        return

    print("The content of the encoded data is: {}\n".format(encoded_data))

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The content of the decoded data is: {}\n".format(decoded_data))

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))


if __name__ == "__main__":

    input_data = ""

    # *** TEST 1 ***

    print("--- Test 1 ---")

    input_data = "The bird is the word"

    print_test_results(input_data)

    """
    The content of the data is: The bird is the word

    The size of the data is: 69

    The content of the encoded data is: 0000010111011010100011111011110001100111010110101110110000110001111011

    The size of the encoded data is: 36

    The content of the decoded data is: The bird is the word

    The size of the decoded data is: 69
    """

    # *** TEST 2 ***

    print("--- Test 2 ---")

    input_data = """His name was Gaal Dornick and he was just a country boy who had never seen Trantor before.
    That is, not in real life. He had seen it many times on the hyper-video, and occasionally in tremendous
    three-dimensional newscasts covering an Imperial Coronation or the opening of a Galactic Council."""

    print_test_results(input_data)

    """
    The content of the data is: His name was Gaal Dornick and he was just a country boy who had never seen Trantor before.
    That is, not in real life. He had seen it many times on the hyper-video, and occasionally in tremendous
    three-dimensional newscasts covering an Imperial Coronation or the opening of a Galactic Council.

    The size of the data is: 349

    The content of the encoded data is: 011001010001111100110111001011111110000110001100111110001101001100110010010001011000110101111011011000011110111000100110011010100100100111110000110001100111110010110000011011111110101001100000111110100110111101010111110101101000100010101010110100011000100111010001001111000100100110111101011100111011110001111111101110110100011101111110110011010101101011110000100010111010110011010111101110101110101110100000000001110111001111000101001000111110110011001101101001010010001101001111011101100100100010010100010110011110101110100011001011100010011110001001001111111101110110100100001010010111111001101101101000101100010111111101111100101011010001011001111100010011101101010000111011110011100110111001000010011110101001100110011001101010010010100111101111110011111100010101101110010010100101011010010001101000101111101110101111111011010100110100110111111101110100000000001011001111110111011100111001010011000101111111011011111110001010110111001001000110111100110001111101111110011111010111111000111110101011100111011110100011010110101001100110100011100001011110100001110111101000110010010000100011101011110101011011100010110001010110100101011110000101100111110001010010000111011011000110101101010010101011001001100000110100110010010110001111010110000111100010001110100110111101011111000100101011101

    The size of the encoded data is: 200

    The content of the decoded data is:
    His name was Gaal Dornick and he was just a country boy who had never seen Trantor before.
    That is, not in real life. He had seen it many times on the hyper-video, and occasionally in tremendous
    three-dimensional newscasts covering an Imperial Coronation or the opening of a Galactic Council.

    The size of the decoded data is: 349
    """

    # *** TEST 3 ***

    print("--- Test 3 ---")

    input_data = ""

    print_test_results(input_data)

    """
    No input data
    """

    # *** TEST 4 ***

    print("--- Test 4 ---")
    input_data = "aaaaaa"

    print_test_results(input_data)

# Resources:
# https://www.studytonight.com/data-structures/huffman-coding
# https://www.cs.cmu.edu/~tcortina/15-121sp10/Unit06B.pdf
