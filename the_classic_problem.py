# https://codeforces.com/contest/464/problem/E

import heapq

def dijkstra(adj_list, start, target):
    n = len(adj_list)
    distance = [float('inf')] * n
    prev = [-1] * n
    distance[start] = 0

    heap = [(0, start)]
    while heap:
        dist, node = heapq.heappop(heap)
        if node == target:
            break

        if dist > distance[node]:
            continue

        for neighbor, weight in adj_list[node]:
            new_dist = distance[node] + weight
            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                prev[neighbor] = node
                heapq.heappush(heap, (new_dist, neighbor))

    if distance[target] == float('inf'):
        return None

    path = []
    curr = target
    while curr != -1:
        path.append(curr)
        curr = prev[curr]

    return distance[target], path[::-1]

def main():
    n, m = map(int, input().split())

    adj_list = [[] for _ in range(n)]
    for _ in range(m):
        u, v, x = map(int, input().split())
        adj_list[u-1].append((v-1, 2**x))
        adj_list[v-1].append((u-1, 2**x))

    s, t = map(int, input().split())

    result = dijkstra(adj_list, s-1, t-1)
    if result is None:
        print(-1)
    else:
        dist, path = result
        print(dist % 1000000007)
        print(len(path))
        print(" ".join(str(x+1) for x in path))

if __name__ == "__main__":
    main()
