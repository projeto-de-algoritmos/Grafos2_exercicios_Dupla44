# https://www.beecrowd.com.br/judge/pt/problems/view/1764

def initialize_set(n):
    parent = list(range(n))
    rank = [0] * n
    return parent, rank

def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1

def kruskal(n, edges):
    parent, rank = initialize_set(n)
    edges.sort()

    total_cost = 0

    for cost, (u, v) in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            total_cost += cost

    return total_cost

while True:
    x, y = map(int, input().split())

    if x == y == 0:
        break

    edges = []
    for _ in range(y):
        a, b, cost = map(int, input().split())
        edges.append((cost, (a, b)))

    total_cost = kruskal(x, edges)
    print(total_cost)
