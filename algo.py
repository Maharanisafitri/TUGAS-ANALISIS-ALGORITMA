import heapq

import heapq

def dijkstra(graf, start):
    jarak = {simpul: float('inf') for simpul in graf}
    jarak[start] = 0
    heap = [(0, start)]
    while heap:
        (jarak_saat_ini, simpul_saat_ini) = heapq.heappop(heap)
        if jarak_saat_ini > jarak[simpul_saat_ini]:
            continue
        for tetangga, bobot in graf[simpul_saat_ini].items():
            jarak_tetangga = jarak_saat_ini + bobot
            if jarak_tetangga < jarak[tetangga]:
                jarak[tetangga] = jarak_tetangga
                heapq.heappush(heap, (jarak_tetangga, tetangga))
    return jarak

graf = {'A': {'B': 3, 'D': 4},
        'B': {'A': 3, 'D': 2, 'E': 6},
        'C': {'E': 1},
        'D': {'A': 4, 'B': 2, 'E': 5},
        'E': {'B': 6, 'C': 1, 'D': 5}}

print(dijkstra(graf, 'A')) 

