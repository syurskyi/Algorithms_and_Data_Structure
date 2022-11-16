class Graph:
    def __init__(self):
        self.adj_list = {}  # dict

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = [] # lsit
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self,v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False




my_graph = ?
?.a..'A'
?.a..'B'
?.a..'C'
?.a..'D'

?.a..'A','B'
?.a..'A','C'
?.a..'A','D'
?.a..'B','D'
?.a..'C','D'


print('Graph before remove_vertex():')
?.p..


?.r.. 'D'


print('\nGraph after remove_vertex():')
?.p..



"""
EXPECTED OUTPUT:
----------------
    Graph before remove_vertex():
    A : ['B', 'C', 'D']
    B : ['A', 'D']
    C : ['A', 'D']
    D : ['A', 'B', 'C']

    Graph after remove_vertex():
    A : ['B', 'C']
    B : ['A']
    C : ['A']

"""