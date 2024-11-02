from scipy.cluster.hierarchy import DisjointSet

disjoint_set = DisjointSet([1, 2, 3, 'a', 'b'])
disjoint_set.merge(1, 2)
disjoint_set.merge(3, 'a')
disjoint_set.merge('a', 'b')
print(disjoint_set.connected(1, 2))
print(disjoint_set.connected(1, 'b'))
print(list(disjoint_set))
print(disjoint_set.subsets())
print(disjoint_set.subset('a'))
print(disjoint_set.subset_size('a'))