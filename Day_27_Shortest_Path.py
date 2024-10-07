from collections import deque

def bfs_shortest_path(graph, start, target):
    queue = deque([start])
    visited = set([start])
    
    predecessor = {start: None}
    
    while queue:
        current_node = queue.popleft()
        
        if current_node == target:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = predecessor[current_node]
            return path[::-1]  
        
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                predecessor[neighbor] = current_node
    
    return "No path exists"

# Example graph and nodes
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2, 4],
    4: [3]
}

start = 0
target = 4

shortest_path = bfs_shortest_path(graph, start, target)
print(shortest_path)
