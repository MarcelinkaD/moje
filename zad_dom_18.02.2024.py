def dfs(graf, v, odw):
    odw[v] = True
    for sasiad in graf[v]:
        if not odw[sasiad]:
            dfs(graf, sasiad, odw)

n, m = map(int, input().split())
graf = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    
    graf[a].append(b)
    graf[b].append(a)
    
q = int(input())

for _ in range(q):
    a, b = map(int, input().split())
    odw = [False for _ in range(n + 1)]
    dfs(graf, a, odw)
    if odw[b]:
        print("TAK")
    else:
        print("NIE")