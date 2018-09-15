"""The user interaction file. Will probably move this elsewhere later on"""
from utils import get_private_key, get_public_key

class User(object):
    def __init__(self, pass_phrase, host, port, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self._private_key = get_private_key(pass_phrase)
        self._public_key = get_public_key(pass_phrase)
        self._host = host
        self._port = port

    @property
    def private_key(self):
        return self._private_key
    
    @property
    def public_key(self):
        return self._public_key
    
    def create_block(self):
        pass

    def mine(self):
        pass
    
    def __repr__(self):
        return self.public_key
    
    def __str__(self):
        return self.public_key
    

class Node(object):
    _neighbours = []
    # neighbours contain the list of neighbouring users

    def __init__(self):
        """Use firebase to get few ip addresses"""
        pass


class Network(Node):
    def __init__(self, *args, **kwargs):
        super(Network, self).__init__(*args, **kwargs)
        pass

    def join(self):
        pass
    
    def sync(self, blockchain):
        """To sync the blockchain. The one with the longer chain size wins.
        args:
            blockchain: The global blockchain object
        """
        pass
    
    def consensus(self, block):
        pass