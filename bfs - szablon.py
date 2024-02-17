import queue as q

def BFS(graf, n, od):
    odw = [0 for _ in range(n + 1)]
    kol = q.Queue()
    kol.put(od)
    odw[od] = 1
    
    while not kol.empty():
        u = kol.get()
        for sasiad in graf[u]:
            if odw[sasiad] == 0:
                kol.put(sasiad)
                odw[sasiad] = 1

def main():
    n, k = map(int, input().split())
    graf = {}
    
    for _ in range(k):
        a, b = map(int, input().split())
        graf[a] = b
    
        
    
main()