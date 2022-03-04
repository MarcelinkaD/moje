def setDict( x ):
    y = dict.fromkeys( x, None )
    for i in y:
        c =[]
        for m in range(1,i // 2 + 1):
            if(i % m == 0):
                c.append(i)
        if len(c) == 2:
            y[i] = "prime"
    return y

print(setDict([31, 100, 40, 72, 2, 45, 53, 52, 23, 63, 3, 41, 7, 1, 99, 47, 38, 25, 87, 24, 26, 21]))