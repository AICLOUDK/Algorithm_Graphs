import sys

def acyclic(adj):
    n = len(adj)
    M = [0] * n

    def dfs(v):
        M[v] = 1

        for H in adj[v]:
            if M[H] == 1:
                return True
            if M[H] == 0:
                if dfs(H):
                    return True

        M[v] = 2
        return False

    for i in range(n):
        if M[i] == 0:
            if dfs(i):
                return 1

    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))