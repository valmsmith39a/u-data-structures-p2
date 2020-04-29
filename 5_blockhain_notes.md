Blockchain:

Sequential chain of records, similar to a linked list

Each block contains some information and how it relates to the other blocks in the chain

Each block contains 1. a cryptographic hash of the previous block 2. timestamp and 3. transaction data

SHA-256 hash (security hash algorithm), Greenwich Mean Time, text strings as data

import hashlib

def calc_hash(self):
      sha = hashlib.sha256()

      hash_str = "We are going to encode this string of data!".encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()


class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()





