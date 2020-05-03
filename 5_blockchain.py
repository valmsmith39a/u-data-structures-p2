import hashlib
from datetime import datetime


class Block:
    """
    This is a class to create a node to store timestamp, previous hash value and some data.

    Attributes:
        timestamp (str): timestamp when block is created
        data (str): some data stored by the user
        previous_hash (str): hash value of previous block
        next (class: Block): refence to the next block
    """

    def __init__(self, data, prev_block=None):
        self.timestamp = datetime.now()
        self.data = data
        self.hash = self.calc_hash(data)
        self.previous_hash = prev_block.hash if prev_block else None
        self.next = None

    def calc_hash(self, data):
        sha = hashlib.sha256()
        hash_str = data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


class Blockchain:
    """
    This is a class to create a linked list data structure for a blockchain

    Attributes:
        head (class: Block): node tracking the front of the blockchain linked list.
    """

    def __init__(self):
        self.head = None

    def append_block(self, data):
        if self.head is None:
            self.head = Block(data)
            return

        block = self.head

        while block.next != None:
            block = block.next

        block.next = Block(data, block)
        self.head = block.next
        return


block_chain = Blockchain()

print("--- Test 1 ---")
block_chain.append_block('block 1 data')
print(block_chain)
print(block_chain.head)
print(block_chain.head.data)
print(block_chain.head.timestamp)
print(block_chain.head.previous_hash)
# <__main__.Blockchain object at 0x1102757d0>
# <__main__.Block object at 0x110275810>
# block 1 data
# 2020-05-02 19:23:18.413513
# None

# print("--- Test 2 ---")
block_chain.append_block('block 2 data')
print(block_chain)
print(block_chain.head)
print(block_chain.head.data)
print(block_chain.head.timestamp)
print(block_chain.head.previous_hash)
# <__main__.Blockchain object at 0x1102757d0>
# <__main__.Block object at 0x1102758d0>
# block 2 data
# 2020-05-02 19:23:18.413610
# 85d9a6a0536c9e84182261e6bd549c4dc462a4977f32822b30e06dd66935b77e

# print("--- Test 3 ---")
block_chain.append_block('block 3 data')
print(block_chain)
print(block_chain.head)
print(block_chain.head.data)
print(block_chain.head.timestamp)
print(block_chain.head.previous_hash)
# <__main__.Blockchain object at 0x1102757d0>
# <__main__.Block object at 0x110275810>
# block 3 data
# 2020-05-02 19:23:18.413645
# 4527648a3fbd8dd06e3018b70fc9661c5e8bfe5b1e6dab5b9f700dfaca517085
