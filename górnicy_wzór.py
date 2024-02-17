from decimal import Decimal as D

def zaokrlag(x, dff5):
    if x + dff5 == int(x) + 1:
        return int(x)
    else:
        return int(round(x, 0))

def main():
    n, a, b = map(int, input().split())
    dff5 = D.from_float(0.5)
    
    dn = D.from_float(n)
    da = D.from_float(a)
    db = D.from_float(b)
    rzda = zaokrlag(da / dn, dff5)
    rzdb = zaokrlag(db / dn, dff5)

    while rzda != rzdb:
        if rzda > rzdb:
            da = D.from_float(rzda)
            rzda = zaokrlag(da / dn, dff5)
        else:
            db = D.from_float(rzdb)
            rzdb = zaokrlag(db / dn, dff5)
            
    print(rzda)
    
main()
