import queue as q

def DFS(w, graf):
    odw = [False] * len(graf)
    odw[w] = True
    kolejka = q.Queue()

    kolejka.put(w)

    while not kolejka.empty():
        u = kolejka.get()
        for sasiad in graf[u]:
            if not odw[sasiad]:
                kolejka.put(sasiad)
                
        odw[u] = True
        
    return odw

