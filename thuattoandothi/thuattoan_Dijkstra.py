import heapq

def dijkstra(graph, start):
    queue = []
    heapq.heappush(queue, (0, start))
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
print("\nDijkstra's shortest paths from A:")
distances = dijkstra(graph, 'A')
for vertex, distance in distances.items():
    print(f"Distance from A to {vertex}: {distance}")
