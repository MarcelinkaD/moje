def brut():
    n, m = map(int, input().split())
    schodki = list(map(int, input().split()))
    ludki = list(map(int, input().split()))
    w = []
    ostatni = n
    for i in range(m):
        for k in range(ostatni):
            if ludki[i] <= schodki[k] or ostatni <= k:
                ostatni = k
                wyn = k
                break
            else:
                wyn = k + 1
        
        w.append(wyn)
            
    print(w)

brut()