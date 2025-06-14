import sys
import queue

def distt(adj, s, t):
    n = len(adj)
    dist = [-1] * n
    dist[s] = 0

    q = queue.Queue()
    q.put(s)

    while not q.empty():
        Va = q.get()

        if Va == t:
            return dist[t]

        for Ma in adj[Va]:
            if dist[Ma] == -1:
                dist[Ma] = dist[Va] + 1
                q.put(Ma)

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distt(adj, s, t))