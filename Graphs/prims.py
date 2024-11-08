class Node:
    def __init__(self,key):
        self.val=key

def prims(adj_list,start_node):
    graph={}
    for i in range(len(adj_list)):
        graph[i] = adj_list[i]
    print("graph=",graph)
    visited = set()
    visited.add(start_node)
    print("visited=",visited)
    edges = []
    while visited:
        min_edge=min()
