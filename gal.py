def nu():
    n, h = map(int, input().split())
    ucie = list(map(int, input().split()))
    wy = 0
    
    for i in ucie:
        if(i < h):
            h = i
            wy += 1
            
    print(wy)
    
nu()
