import transporters
import networkx as nx
#...

class ComparResult:
    def __init__(self, transporter1, transporter2, similarity):
        self.transporter1 = transporter1
        self.transporter2 = transporter2
        self.similarity = similarity
        #TODO

def cotrie(transporter1):
    return 0
    #TODO

def analyze(transporter1, transporter2):
    #TODO
    return ComparResult(transporter1, transporter2, similarity)