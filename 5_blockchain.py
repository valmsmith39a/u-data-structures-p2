import hashlib


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = "Make it work, make it right, make it fast.".encode('utf-8')

        sha.update = (hash_str)

        return sha.hexdigest()
