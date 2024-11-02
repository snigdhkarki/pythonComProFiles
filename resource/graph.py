import networkx as nx

G = nx.DiGraph()
G.add_edges_from([(1, 2), (1, 5), (2, 4), (5, 4),(9,10),(10,8)])

# bfs
bfs = list(nx.bfs_edges(G, source=1))
print("BFS tree:", bfs)  
print(dict(nx.single_source_all_shortest_paths(G, source=1)))

# coag/stronglyConnectedComponent for directed/undirected graph by making all directed edge to undirected edge
components = list(nx.weakly_connected_components(G)) #for undirected graph remove "weakly_" / replace with "strongly_" for strongly connected
weekly_connected_subgraphs = []
for component in components:
    subgraph = G.subgraph(component) 
    weekly_connected_subgraphs.append(subgraph) 
print(components)
for i, tree_edges in enumerate(weekly_connected_subgraphs):
    print(f"Weakly Connected Component {i + 1} edges:")
    print(list(tree_edges.edges()))



#check if acyclic
print("Graph G is acyclic:", nx.is_directed_acyclic_graph(G))

#topological sort
topo_sort = list(nx.topological_sort(G))
print("Topological Sort:", topo_sort) 

#Minimum spanning tree
Gu = nx.Graph()
# Add edges and weights
edges = [
    (1, 2, 1),
    (1, 3, 3),
    (2, 3, 1),
    (2, 4, 6),
    (3, 4, 5),
    (4, 5, 2),
]
Gu.add_weighted_edges_from(edges)
mst = nx.minimum_spanning_tree(Gu)
print("Edges in the Minimum Spanning Tree:")
for edge in mst.edges(data=True):
    print(edge)

#Dijkstra's algorithm
source_node = 1
paths = nx.single_source_dijkstra_path(Gu , source_node)
distances = nx.single_source_dijkstra(Gu , source_node)[0]
print(f"Shortest paths from node {source_node}:")
for target, path in paths.items():
    print(f"Path to {target}: {path}, Distance: {distances[target]}")

#bellman_ford_shortest_path
def bellman_ford_shortest_path(graph, source):
    try:
        paths = nx.single_source_bellman_ford_path(Gu , source_node)
        distances = nx.single_source_bellman_ford(Gu , source_node)[0]
        return paths, distances
    except nx.NetworkXUnbounded:
        print("Graph contains a negative weight cycle.")
        return None, None
source_node = 1
paths, distances = bellman_ford_shortest_path(Gu, source_node)
if distances is not None:
    print(f"Shortest paths from node {source_node}:")
    for target, path in paths.items():
        print(f"Path to {target}: {path}, Distance: {distances[target]}")

#shortest path all pair of vertices
shortest_paths =dict(nx.all_pairs_shortest_path(Gu))
for source, targets in shortest_paths.items():
    for target, path in targets.items():
        print(f"Shortest path from {source} to {target}: {path}")