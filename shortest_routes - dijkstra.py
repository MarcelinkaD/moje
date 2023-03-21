import heapq

N = 200003
inf = 10**18
adj = [[] for _ in range(N)]
dist = [inf] * N

def dijkstra():
    dist[1] = 0
    pq = [(0, 1)]
    heapq.heapify(pq)
    while pq:
        d, u = heapq.heappop(pq)
        if dist[u] < d:
            continue
        for c, v in adj[u]:
            if dist[v] <= c+d:
                continue
            else:
                dist[v] = c+d
                heapq.heappush(pq, (dist[v], v))

n, m = map(int, input().split())

for i in range(m):
    a, b, w = map(int, input().split())
    adj[a].append((w, b))

dijkstra()

for i in range(1, n+1):
    print(dist[i], end=" ")

