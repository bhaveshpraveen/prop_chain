from block import Block
from transaction import Transaction

from utils import validate_argument_type

class BlockChain(object):
    _blockchain = []

    def __init__(self):
        super(BlockChain, self).__init__()
        self.create_genesis_block()

    @property
    def blockchain(self):
        return self._blockchain

    @validate_argument_type(Block)
    def append(self, block):
        """Appends the block to the blockchain
        args: 
            block: Block object
        """
        self.blockchain.append(block)

    def get_last_block(self):
        return self.blockchain[-1]
    
    # this function is probably unneccesary
    def create_genesis_block(self):
        """Creates the first block with dummy data."""
        block = Block(
            block_no=1,
            transactions=Transaction('James', 'Murray', 'Chinatown'),
            nonce=0,
            previous_hash=0
        )
        self.append(block)

