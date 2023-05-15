
#https://moj.naquadah.com.br/contests/bcr-EDA2-2022_1-trabalho/handshakes-rule

import heapq

def dijkstra(graph, start, end):
    # Inicialização
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        # Verifica se já encontrou o destino
        if current_node == end:
            return dist[current_node]

        # Verifica se a distância atual é menor que a distância armazenada
        if current_dist > dist[current_node]:
            continue

        # Explora os vizinhos do nó atual
        for neighbor, weight in graph[current_node].items():
            new_dist = current_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    # Não há conexão entre as duas pessoas
    return -1

# Função para criar o grafo com base nas informações de apertos de mão
def create_graph(N, M):
    graph = {}
    for _ in range(N):
        name = input().strip()
        graph[name] = {}

    for _ in range(M):
        V, W = input().split()
        # Adiciona a aresta nos dois sentidos, pois o grafo é não direcionado
        graph[V][W] = 1
        graph[W][V] = 1

    return graph

# Entrada de dados
S, E = input().split()
N, M = map(int, input().split())

graph = create_graph(N, M)

# Executa o algoritmo de Dijkstra para encontrar o número mínimo de apertos de mão
minimum_handshakes = dijkstra(graph, S, E)

# Imprime o resultado
print(minimum_handshakes)
