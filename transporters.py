import trie

class ABC_transporters:
    '''
    TODO: comments
    '''
    def __init__(self, name, transporters, signature):
        self.name = name
        self.transporters = transporters
        self.suffix_tree = trie.trie(transporters)
        self.signature = signature

    def dump(self):
        '''
        TODO:
        Save all transporters and their trie to a file (zip?)
        '''
        return True

    def load(self):
        '''
        TODO: 
        Load transporters from file (separate function, not in class?)
        '''
        return True