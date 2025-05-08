import sys
import math
import heapq

def min_dist(x, y):
    n = len(x)
    dist = [float('inf')] * n
    dist[0] = 0
    Ma = [False] * n
    pq = [(0, 0)]

    sub_w = 0

    while pq:
        d, u = heapq.heappop(pq)

        if Ma[u]:
            continue

        Ma[u] = True
        sub_w += d

        for v in range(n):
            if not Ma[v]:
                w = math.sqrt((x[u] - x[v])**2 + (y[u] - y[v])**2)
                if w < dist[v]:
                    dist[v] = w
                    heapq.heappush(pq, (dist[v], v))

    return sub_w

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(min_dist(x, y)))