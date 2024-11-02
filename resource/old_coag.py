class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            if v not in self.graph[u]:
                self.graph[u].append(v)
        else:
            self.graph[u] = [v]        


def coag(current,visited):       
    visited_g.append(current)    
    visited.append(current)  
    nodes = [current]
    for child in g.graph[current]:
        if child not in visited and Map[child]=='O':  
            nodes+=coag(child,visited)        
    return nodes                     


N = 4
M = 12
g = Graph()
for x in range(N):
    for y in range(M):
        for i,j in [(-1,-1), (-1,0),(-1,1), (0,-1),(0,1),(1,-1),(1,0),(1,1)]:
            if not (x+i<0 or x+i>=N or y+j<0 or y+j>=M):
                g.add_edge((x,y), (x+i,y+j))
mp = []
for _ in range(N):
    str = input()
    mp += [list(str)]
Map = {}
for i in range(N):
    for j in range(M):
        Map[(i,j)] = mp[i][j]


visited_g = []  
coag_dict = {}
coag_id = 0 

for i in range(N):
    for j in range(M):
        if (i,j) not in visited_g and Map[(i,j)] == 'O':
            coag_dict[coag_id]= coag((i,j),[])                 
            coag_id += 1
print(coag_dict)