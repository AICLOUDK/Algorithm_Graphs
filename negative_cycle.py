import sys
def negative_cycle(adj, cost):
    n = len(adj)
    dist = [0] * n
    for _ in range(n):
        for u in range(n):
            for i, v in enumerate(adj[u]):
                if dist[u] + cost[u][i] < dist[v]:
                    dist[v] = dist[u] + cost[u][i]
    for u in range(n):
        for i, v in enumerate(adj[u]):
            if dist[u] + cost[u][i] < dist[v]:
                return 1
    return 0

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
    print(negative_cycle(adj, cost))
