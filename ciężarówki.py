# https://szkopul.edu.pl/c/olimpiada-poziom-ii-202223/p/bra/18442/

from sys import stdin
input = stdin.readline

def main():
    n, a, b = map(int, input().split())
    os = []
    w = 0
    maxi = -1
    
    for _ in range(n):
        x, pr = map(int, input().split())
        os.append([x, pr])
        maxi = max(maxi, pr)
        
    nesseser = a
    jaki = -1
    naj_czas = 1e18
    
    for i in range(n):
        t = abs(a - os[i][0]) / os[i][1]
        if t < naj_czas:
            naj_czas = t
            jaki = i
            
    for i in range(n):
        if i == jaki:
            os[i][0] = a
            w += naj_czas
        else:
            if a < os[i][0]:
                os[i][0] -= os[i][1] * naj_czas
            else:
                os[i][0] += os[i][1] * naj_czas
            
    
    while nesseser != b:
        if (os[jaki][1] == maxi) == False:
            for i in range(n):
                if i == jaki:
                    continue
                else:
                    if a < b:
                        if os[i][1] > os[jaki][1] and os[i][0] > os[jaki][0]:
                            v0, v1 = os[jaki][1], os[i][1]
                            s1 = os[i][0] - os[jaki][0]
                            x = (s1 * v0) / (v1 + v0)
                            t = x / v0
                            w += t
                            nesseser = x
                            os[i][0] = x
                            os[jaki][0] = x
                            jaki = i
                    else:
                        if os[i][1] > os[jaki][1] and os[i][0] < os[jaki][0]:
                            v0, v1 = os[jaki][1], os[i][1]
                            s1 = os[i][0] - os[jaki][0]
                            x = (s1 * v0) / (v1 + v0)
                            t = x / v0
                            w += t
                            nesseser = x
                            os[i][0] = x
                            os[jaki][0] = x
                            jaki = i
        else:
            v = os[jaki][1]
            odl = abs(b - os[jaki][0])
            t = odl / v
            w += t
            nesseser = b
    
    w = abs(w)
    print("%.9f" % w)
                    
main()