# class Graph:
#     def __init__(self):
#         self.graph = {}

#     def add_edge(self, u, v):
#         if u in self.graph:
#             self.graph[u].append(v)
#         else:
#             self.graph[u] = [v]
#         if v in self.graph:
#             self.graph[v].append(u)
#         else:
#             self.graph[v] = [u]
# g = Graph()
# g.add_edge(1,2)
# g.add_edge(1,4)
# g.add_edge(1,5)
# g.add_edge(2,4)
# g.add_edge(2,3)
# g.add_edge(5,7)
# g.add_edge(5,6)
# g.add_edge(6,3)
# g.add_edge(7,3)
# g.add_edge(4,3)



# def _dfs_helper(current, end, path): 
#     #input:current node, destination node and path already travelled
#     #outpus: list of paths aviablable     
#     if current == end:
#         return [path +[current]]
#     else:     
#         paths = []   
#         for neighbor in g.graph[current]:
#             if neighbor not in path:  
#                 paths = paths+_dfs_helper(neighbor, end, path+[current])
#         return paths


# print(_dfs_helper(1,3,[]))

