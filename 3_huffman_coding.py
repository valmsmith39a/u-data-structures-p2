import sys
from heapq import heappush, heappop


def huffman_encoding(data):
    # relative frequency map
    rf_map = get_relative_frequencies(data)
    # build queue of nodes
    queue = []
    for rf in rf_map:
        freq = rf[0]
        char = rf[1]
        queue.append(Node(char, freq))

    pass


def huffman_decoding(data, tree):
    pass


def get_relative_frequencies(data):
    rf_dict = dict()
    rf = []
    total = len(data)

    for c in data:
        if c in rf_dict:
            rf_dict[c] += 1
        else:
            rf_dict[c] = 1

    for key, value in rf_dict.items():
        rf_value = round(value / total, 3)
        rf.append((rf_value, key))

    rf.sort(key=lambda x: x[1])

    return rf


class Node(object):

    def __init__(self, char=None, freq=None, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    print(huffman_encoding(a_great_sentence))
    # encoded_data, tree = huffman_encoding(a_great_sentence)

    # print("The size of the encoded data is: {}\n".format(
    #     sys.getsizeof(int(encoded_data, base=2))))
    # print("The content of the encoded data is: {}\n".format(encoded_data))

    # decoded_data = huffman_decoding(encoded_data, tree)

    # print("The size of the decoded data is: {}\n".format(
    #     sys.getsizeof(decoded_data)))
    # print("The content of the encoded data is: {}\n".format(decoded_data))
