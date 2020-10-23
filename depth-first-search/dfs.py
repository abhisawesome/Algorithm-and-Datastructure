graphs = {"A":["B","C", "D"],
           "B":["E"],
           "C":["F","G"],
           "D":["H"],
           "E":["I"],
           "F":["J"]}

def dfs(graph,root,visited=[]):
    
    if root not in visited:
        # Mark as visited
        visited.append(root)
        # Backtracking
        if root not in graph:
            return visited
        for node in graph[root]:
            visited = dfs(graph,node,visited)
    return visited

print(dfs(graphs,'A'))

