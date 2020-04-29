import hashlib


class Block:

    def __init__(self, data):
        self.timestamp = 'hardcoded timestamp'
        self.data = data
        self.previous_hash = 'hardcoded previous hash'
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = "Make it work, make it right, make it fast.".encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


class Blockchain:

    def __init__(self):
        self.head = None

    def append_block(self, data):
        if self.head is None:
            self.head = Block(data)
            return

        block = self.head

        while block.next != None:
            block = block.next

        block.next = Block(data)
        self.head = block.next
        return


block_chain = Blockchain()
print(block_chain)
block_chain.append_block('block 1 data')
print(block_chain)
block_chain.append_block('block 2 data')
print(block_chain)
block_chain.append_block('block 3 data')
print(block_chain)
