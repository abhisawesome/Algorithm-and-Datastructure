graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}


def bfs(graph,root):
    
    # Identify visited node
    visited=[]
    queue=[root]


    while queue:
        # Select the node (Pop from the first)
        node = queue.pop(0)
        # Check if node visited
        if node not in visited:
           
            # Add the node as visited
            visited.append(node)

            # Get the adjacent vertex
            adjacentNode = graph[node]

            print({node:adjacentNode})
            # Add the adjacent vertex to queue
            for adNode in adjacentNode:
                queue.append(adNode)
    return visited


print(bfs(graph,'A'))

