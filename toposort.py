import sys

def dfs(adj, used, order, x):
    used[x] = 1
    for H in adj[x]:
        if used[H] == 0:
            dfs(adj, used, order, H)
    used[x] = 2
    order.append(x)

def toposort(adj):
    used = [0] * len(adj)
    order = []
    for i in range(len(adj)):
        if used[i] == 0:
            dfs(adj, used, order, i)
    order.reverse()
    return order

input = sys.stdin.read()
data = list(map(int, input.split()))
n, m = data[0:2]
data = data[2:]
edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
adj = [[] for _ in range(n)]
for (a, b) in edges:
    adj[a - 1].append(b - 1)
order = toposort(adj)
for x in order:
    print(x + 1, end=' ')