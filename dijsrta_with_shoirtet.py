class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        ans = 0
        min_cost = collections.defaultdict(list)
        graph = collections.defaultdict(list)

        def build_graph():
            for s, d , c in zip(original , changed , cost):
                graph[ord(s)-97].append((ord(d)-97, c))
        
        def dijstra(src):
            dist = [float("inf")] * 26
            dist[src] = 0

            min_heap = []
            heapq.heappush(min_heap  , (0, src))

            while min_heap:
                cur , node = heapq.heappop(min_heap)


                for neigh , cost in graph[node]:
                    if dist[neigh] > dist[node] + cost:
                        dist[neigh] =  dist[node] + cost
                        heapq.heappush(min_heap , (dist[neigh] , neigh))

            return dist

        build_graph()
        for i in range(0,26):
            val = dijstra(i)
            min_cost[chr(i+97)] = val

        t  = ''
        for i in range(0,len(source)):
            s = source[i]
            d = target[i]

            if min_cost[s][ord(d)-97] != float('inf'):
                ans = ans + min_cost[s][ord(d)-97]
                t += d

        if t == target:
            return(ans)
        else:
            return(-1)
