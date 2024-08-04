There is a map of cities - like a real world country's map. Some cities have roads between them, and it takes a known time to traverse each road.I'm in city A and have a list of my favorite cities [F1..Fn]. Give an efficient algoritha to decide which of my favorite cities I can get to the fastest.

Solved it using dijktra's with priority queue

Problem was finding time complexcity. The algorithm I wrote with with min heap was traversing the same node again and again. So had to make it more efficient. But inspite of doing that the time complexcity was coming out to be (V+E)logE and not (V+E)logV which I'd learnt. Turns out E = V*(V-1), hence (V+E)2log(V). So got a bit confused.

The interviewer was too good in time complexcity analysis.

google

import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_dist, u = heapq.heappop(priority_queue)
        
        if current_dist > dist[u]:
            continue
        
        for neighbor, weight in graph[u]:
            distance = current_dist + weight
            
            # If a shorter path is found
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return dist

def find_closest_favorite_city(graph, start, favorite_cities):
    # Run Dijkstra's algorithm from the start city
    distances = dijkstra(graph, start)
    
    # Find the closest favorite city
    closest_city = None
    min_distance = float('inf')
    
    for city in favorite_cities:
        if distances[city] < min_distance:
            min_distance = distances[city]
            closest_city = city
            
    return closest_city, min_distance

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

start_city = 'A'
favorite_cities = ['B', 'C', 'D']

closest_city, min_distance = find_closest_favorite_city(graph, start_city, favorite_cities)
