import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout
import pydot

class trie:
    '''
    Trie data structure.
    G: NX exemplar of a graph.
    words: words used to build tree
    '''
    def __init__(self, words):
        self.G = nx.DiGraph()
        self.words = words
        self.build()
    

    def build(self):
        '''
        Build trie from words.
        '''
        self.G.add_nodes_from([(0, {"terminal": False})])
        last_node = 1
        for word in self.words:
            curr_node = 0
            print(word)
            for i in range(len(word)):
                print("curr_node", curr_node)
                print('word[i]', word[i])
                add_edge = True
                for edge in self.G.edges(curr_node):
                    print(edge)
                    if self.G[edge[0]][edge[1]]["letter"] == word[i]:
                        print(self.G[edge[0]][edge[1]]["letter"])
                        curr_node = edge[1]
                        add_edge = False
                        break
                if add_edge == True:
                    print('adding letter ', word[i])
                    is_terminal = False
                    if i == len(word) - 1:
                        is_terminal = True
                    self.G.add_nodes_from([(last_node, {"terminal" : is_terminal})])
                    self.G.add_edge(curr_node, last_node, letter = word[i])
                    curr_node = last_node
                    last_node +=1 



def main():
    '''
    tests    
    '''
    T = trie(["he", "she", "his", "hers"])
    pos = graphviz_layout(T.G, prog="dot")
    edge_lbls = dict([((n1, n2), d['letter']) for n1, n2, d in T.G.edges(data=True)])
    labels = nx.get_node_attributes(T.G, 'terminal')
    nx.draw(T.G, pos, labels = labels)
    nx.draw_networkx_edge_labels(T.G, pos, edge_labels = edge_lbls)
    nx.draw_networkx_nodes(T.G, pos, )
    plt.show()


if __name__ == '__main__':
    main()