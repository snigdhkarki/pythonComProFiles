# Conditions for binary graph:
# 1)  Each node can have only one parent node.
# 2)  Each node can have at most 2 children


# class Node:
#     idstat = 0
#     def __init__(self, data):
#         self.id = Node.idstat
#         Node.idstat += 1
#         self.data = data  
#     def __repr__(self):
#         return "<"+str(self.id)+","+str(self.data)+">"
# class Graph:
#     def __init__(self):
#         self.graph = {}
#         self.parent = {}

#     def add_edge(self, u, v):        
#         if u in self.graph:
#             self.graph[u].append(v)
#         else:
#             self.graph[u] = [v]
#         self.parent[v] = u
    
# def parentof(g,u):
#     return g.parent[u]

        
# def left(g,u):
#     if u in g.graph:
#         if len(g.graph[u])>0:
#             return g.graph[u][0]
#         else:
#             return None
#     else:
#         return None
# def right(g,u):
#     if u in g.graph:
#         if len(g.graph[u])>1:
#             return g.graph[u][1]
#         else:
#             return None
#     else:
#         return None

        
# def treeMax(g, node):
#     if node is None:
#         return float("-inf")
#     else:
#         leftMax = treeMax(g,left(g,node))
#         rightMax = treeMax(g,right(g,node))
#         return max(node.data, leftMax, rightMax)

# g = Graph()
# nodes = [Node(1), Node(2), Node(8), Node(2), Node(4), Node(5), Node(7), Node(1)]
# g.add_edge(nodes[0], nodes[1])
# g.add_edge(nodes[0], nodes[2])
# g.add_edge(nodes[1], nodes[3])
# g.add_edge(nodes[1], nodes[4])
# g.add_edge(nodes[2], nodes[5])
# g.add_edge(nodes[2], nodes[6])
# g.add_edge(nodes[3], nodes[7])


# print(treeMax(g, nodes[0]))
# print(g.graph)
# print(parentof(g, nodes[3]))