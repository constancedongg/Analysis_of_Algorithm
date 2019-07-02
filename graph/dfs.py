'''
Dfs starts from a vertex s, explores the graph as deeply as possible, then backtrack.

Use stack: last-in first-out (LIFO)

Difference between bfs and dfs: dfs uses stack.pop(), bfs uses queue.pop(0) (pop out the first-in element)
'''

# Non-recursive
def dfs_connected_component(graph , start):
    explored = []
    stack = [start]

    while stack:
        node = stack.pop()     # the only difference
        if node not in explored:
            explored.append(node)
            neighbors = graph[node]
            for neighbor in neighbors:
                stack.append(neighbor)
            print(stack)
    return explored


# Recursive
def dfs_recursive(graph , start , path):
    path += [start]
    
    for neighbor in graph[start]:
        if neighbor not in path:
            dfs_recursive(graph , neighbor , path)
    
    return path


# sample graph implemented as a dictionary
graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B' , 'E'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}
# print(dfs_connected_component(graph , 'A'))

print(dfs_recursive(graph , 'A' , []))
