#https://codeforces.com/problemset/problem/25/C

import heapq

def dijkstra(graph, start):
    distances = [float('inf')] * len(graph)
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        dist, vertex = heapq.heappop(pq)

        if dist > distances[vertex]:
            continue

        for neighbor, weight in graph[vertex]:
            new_dist = dist + weight

            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return distances

# Leitura da entrada
n = int(input())
distances = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

# Inicialização do grafo com as distâncias existentes
graph = [[] for _ in range(n)]

# Construção do grafo com as distâncias existentes
for i in range(n):
    for j in range(i+1, n):
        graph[i].append((j, distances[i][j]))
        graph[j].append((i, distances[j][i]))

# Lista para armazenar os resultados
results = []

# Cálculo das distâncias iniciais entre todas as cidades
initial_sum = sum(sum(distances[i]) for i in range(n))
results.append(initial_sum)

# Construção das novas estradas e cálculo das novas distâncias
for _ in range(k):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1

    # Atualização do grafo com a nova estrada
    graph[a].append((b, c))
    graph[b].append((a, c))

    # Aplicação do algoritmo de Dijkstra a partir de cada cidade
    new_distances = []
    for i in range(n):
        new_distances.append(dijkstra(graph, i))

    # Cálculo da nova soma das distâncias
    new_sum = sum(sum(new_distances[i]) for i in range(n)) // 2

    # Adição do resultado à lista
    results.append(new_sum)

# Impressão dos resultados
print(' '.join(map(str, results[1:])))
