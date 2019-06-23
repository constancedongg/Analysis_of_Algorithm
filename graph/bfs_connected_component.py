
'''
BFS starts from a node, then it checks all the nodes at distance one from the starting node, 
then it checks all the nodes at distance two and so on.

To implement the BFS queue a FIFO (First In, First Out) is used. 

Start from the vertex, then loop over all nodes (keep dequeue the first node) till queue is empty;
if a noded is checked before, next;
else, add its neighbors to queue.

https://pythoninwonderland.wordpress.com/2017/03/18/how-to-implement-breadth-first-search-in-python/
'''

# This function to explore all connected components of a graph using BFS, start from the node start

def bfs_connected_component(graph , start):
    explored = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in explored:
            explored.append(node)
            neighbors = graph[node]
            for neighbor in neighbors:
                queue.append(neighbor)
            print(queue)
    return explored





# sample graph implemented as a dictionary
graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B' , 'E'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}
print(bfs_connected_component(graph , 'A'))