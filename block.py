from hashlib import sha256
from time import time, localtime

from transaction import Transaction
from utils import (
    get_all_transactions_as_str,
    validate_argument_type,
    get_local_time,
)

class Block(object):
    def __init__(self, block_no, nonce, previous_hash, transactions=None):
        self.block_no = block_no
        self.transactions = transactions or []
        self.nonce = nonce
        self.previous_hash = previous_hash
        self.timestamp = time()
        self.hash = None
    
    def create_hash(self):
        block_info = "{}{}{}{}{}".format(
            self.block_no,
            self.nonce,
            self.previous_hash,
            self.get_transaction_str(),
            self.timestamp)
        self.hash = sha256(block_info.encode()).hexdigest()

    
    @validate_argument_type(Transaction)
    def append_transactions(self, transaction):
        self.transactions.append(transaction)
        

    def get_transaction_str(self):
        return get_all_transactions_as_str(self)

    @property
    def transactions(self):
        return self.transactions_
    
    @transactions.setter
    def transactions(self, transactions_):
        self.transactions_ = transactions_

    def __str__(self):
        return "{}{}{}{}{}".format(
            self.block_no,
            self.nonce,
            self.previous_hash,
            get_local_time(self.timestamp),
            self.hash
        )