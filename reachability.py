#Uses python3
import sys

def reach(adj, x, y):
    M = [False] * len(adj)

    def dfs(u):
        M[u] = True
        if u == y:
            return True
        for v in adj[u]:
            if not M[v]:
                if dfs(v):
                    return True
        return False

    return 1 if dfs(x) else 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))