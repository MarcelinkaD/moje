import math
import heapq
from collections import deque
from collections import Counter as C
from itertools import accumulate
from dataclasses import dataclass
from sys import stdin
input = stdin.readline

# przykładowy graf reprezentowany przez słownik sąsiedztwa
graph = {
    'a': ['b', 'c'],
    'b': ['d', 'e'],
    'c': ['f'],
    'd': [],
    'e': ['f'],
    'f': []
}

def bfs_path(graph, start, end):
    # kolejka przechowująca wierzchołki do odwiedzenia
    queue = deque([start])
    # słownik zapisujący poprzedników wierzchołków
    predecessors = {start: None}

    while queue:
        # pobierz pierwszy wierzchołek z kolejki
        current = queue.popleft()

        # jeśli dotarliśmy do wierzchołka końcowego, zakończ BFS
        if current == end:
            break

        # przeglądaj sąsiadów wierzchołka bieżącego
        for neighbor in graph[current]:
            if neighbor not in predecessors:
                # zapisz poprzednika sąsiada i dodaj go do kolejki
                predecessors[neighbor] = current
                queue.append(neighbor)

    # zapisz ścieżkę od wierzchołka końcowego do wierzchołka początkowego
    path = []
    while end:
        path.append(end)
        end = predecessors[end]

    # odwróć kolejność wierzchołków, aby uzyskać ścieżkę od początku do końca
    return path[::-1]

# przykładowe wywołanie funkcji bfs_path
print(bfs_path(graph, 'a', 'f'))  # wynik: ['a', 'c', 'f']
