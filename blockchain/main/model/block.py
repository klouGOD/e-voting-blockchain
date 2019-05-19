import hashlib

from time import time

class Block:
  def __init__(self, index, transactions, proof, previous_hash):
    self.index = index
    self.transactions = transactions
    self.proof = proof
    self.timestamp = time()

  @staticmethod
  def hash(block):
    """
    Creates a SHA-256 hash of a Block
    :param block: Block
    """

    # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
    block_string = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()