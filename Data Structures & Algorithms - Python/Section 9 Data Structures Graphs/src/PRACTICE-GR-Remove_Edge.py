class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    ## WRITE REMOVE_EDGE METHOD HERE ##
    #                                 #
    #                                 #
    #                                 #
    #                                 #
    ###################################




my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')

my_graph.add_edge('A','B')
my_graph.add_edge('B','C')
my_graph.add_edge('C','A')

print('Graph before remove_edge():')
my_graph.print_graph()


my_graph.remove_edge('A','C')


print('\nGraph after remove_edge():')
my_graph.print_graph()



"""
    EXPECTED OUTPUT:
    ----------------
    Graph before remove_edge():
    A : ['B', 'C']
    B : ['A', 'C']
    C : ['B', 'A']

    Graph after remove_edge():
    A : ['B']
    B : ['A', 'C']
    C : ['B']
    
"""