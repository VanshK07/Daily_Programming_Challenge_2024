def has_cycle(graph):
    visited = set()
    
    def dfs(v, parent):
        visited.add(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                if dfs(neighbor, v):
                    return True
            elif neighbor != parent:
                return True
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, -1):
                return True
    return False
    
graph_with_cycle = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2]
}

graph_without_cycle = {
    0: [1],
    1: [0, 2],
    2: [1, 3],
    3: [2]
}

print(has_cycle(graph_with_cycle)) 
print(has_cycle(graph_without_cycle)) 
