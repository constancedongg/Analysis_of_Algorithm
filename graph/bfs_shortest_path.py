
'''
Application: 
- Find people at a given distance from a person in social networks.
- Identify all neighbour locations in GPS systems.
- Search whether there’s a path between two nodes of a graph and shortest path.

Time complexity: exponential
Space complexity: even worse, needs high memory
'''
def bfs_shortest_path(graph , start , goal):
    explored = []
    queue = [[start]]

    if start == goal:
        return 'You find it instantly!'

    while queue:

        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbors = graph[node]
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                print(queue)
                if neighbor == goal:
                    return new_path
            explored.append(node)
            
    return 'There is no path between {} and {}'.format(start, goal) 


graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B', 'E'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C'],
         'H': []}
print(bfs_shortest_path(graph , 'A' , 'G'))

print(bfs_shortest_path(graph , 'D' , 'G'))

print(bfs_shortest_path(graph , 'D' , 'H'))