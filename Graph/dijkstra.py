Shortest path between 2 nodes with non negative weights. The graph should not have even a single negative weighted Node. 
def dijkstra(graph, start_node):
    """
    Finds the shortest paths from a start node to all other nodes in a weighted graph.
    
    :param graph: Dict[str, Dict[str, float/int]] - Adjacency list with edge weights.
                  e.g., {'A': {'B': 4, 'C': 2}}
    :param start_node: The starting node
    :return: Dict - Shortest distance from start_node to every other node
    """
    # Track the minimum distance to each node; default to infinity
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0

    # Priority queue stores tuples of (distance, node)
    # Python's heapq is a min-heap, so the smallest distance is popped first
    pq = [(0, start_node)]
    
    # Optional: Track path predecessors if you need to reconstruct the full path
    # predecessors = {node: None for node in graph}

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # If we found a shorter path to current_node already, skip this entry
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If a shorter path to neighbor is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # predecessors[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return distances
