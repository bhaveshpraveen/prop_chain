from block import Block
from transaction import Transaction

def validate_argument_type(arg_type=None):
    def inner(function):
        def wrapper(self, *args, **kwargs):
            for arg in args + tuple(kwargs.values()):
                if not isinstance(arg, arg_type):
                    raise TypeError(
                        "Expected object of type {}." \
                        "Received {}".format(
                            type(arg_type).__name__, 
                            type(arg).__name__)
                    )
            return function(self, *args, **kwargs)
        return wrapper
    return inner


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
    
    def create_genesis_block(self):
        block = Block(
            block_no=1,
            transactions=Transaction('James', 'Murray', 'Chinatown'),
            nonce=0,
            previous_hash=0
        )
        self.append(block)

