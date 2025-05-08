import sys
import queue

def distance(adj, cost, s, t):
    dist = [float('inf')] * len(adj)
    dist[s] = 0
    pq = queue.PriorityQueue()
    pq.put((0, s))

    while not pq.empty():
        d, u = pq.get()

        if d > dist[u]:
            continue

        if u == t:
            return dist[t]

        for i in range(len(adj[u])):
            v = adj[u][i]
            w = cost[u][i]
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                pq.put((dist[v], v))

    return -1 if dist[t] == float('inf') else dist[t]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))