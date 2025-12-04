def dijkstra(graph, start_node):
    distances = {node: float('infinity') for node in graph.nodes()}
    distances[start_node] = 0
    
    previous_nodes = {node: None for node in graph.nodes()}
    
    unvisited = list(graph.nodes())

    while unvisited:
        current_node = min(unvisited, key=lambda node: distances[node])

        if distances[current_node] == float('infinity'):
            break

        for neighbor, attributes in graph[current_node].items():
            weight = attributes.get('weight', 1)
            new_distance = distances[current_node] + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous_nodes[neighbor] = current_node

        unvisited.remove(current_node)

    return distances, previous_nodes


def reconstruct_path(previous_nodes, start, target):
    path = []
    current = target
    
    while current is not None:
        path.append(current)
        if current == start:
            break
        current = previous_nodes[current]
    
    return path[::-1]

