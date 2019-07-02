'''
Dijkstra's algorithm: to find the shortest path between nodes for weighted graph.

Greedy: always form the shortest new s-v path by first following a path to some node u in S, and then a single edge (u, v).
'''

import heapq

def init_distance(graph , s):
    distance = {s: 0}
    for vertex in graph:
        if vertex != s:
            distance[vertex] = float('inf')
    return distance



def dijkstra(graph , s):
    pqueue = []
    heapq.heappush(pqueue , (0 , s))
    explored = []
    parent = {s: None}   # path, from u to v, u -> v, parent = {v: u}
    distance = init_distance(graph, s)

    while len(pqueue) > 0:
        pair = heapq.heappop(pqueue)
        dist = pair[0]
        vertex = pair[1]
        explored.append(vertex)

        nodes = graph[vertex].keys()
        for w in nodes:
            if w not in explored:
                new_dist = dist + graph[vertex][w]
                if  new_dist < distance[w]:
                    heapq.heappush(pqueue , (new_dist , w))
                    parent[w] = vertex  # vertex -> w
                    distance[w] = new_dist

    return parent , distance





graph = {'A': {'B': 5 , 'C': 1},
         'B': {'A': 5 , 'C': 2 , 'D': 1},
         'C': {'A': 1 , 'B': 2 , 'D': 4 , 'E': 8},
         'D': {'B': 1 , 'C': 4 , 'E': 3 , 'F': 6},
         'E': {'C': 8 , 'D': 3},
         'F': {'D': 6}
}


parent , distance = dijkstra(graph , 'A')
print(parent)
print(distance)
'''
{'A': None, 'C': 'A', 'B': 'C', 'E': 'D', 'D': 'B', 'F': 'D'}
'F' <- 'D' <- 'B' <- 'C' <- 'A'
10 <- 4 <- 3 <- 1 <- 0 
'''