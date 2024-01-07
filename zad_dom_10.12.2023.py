import math

def x_do_y(x, y, MOD):
    if y == 0:
        return 1
    else:
        if y % 2 == 1:
            return x * x_do_y(x, y - 1, MOD) % MOD
        else:
            pol = x_do_y(x, y // 2, MOD)
            return pol * pol % MOD

n = int(input())
MOD = int(1e9)
z_zerem = (9 * x_do_y(2, n - 1, MOD)) - 9 #odejmujemy 9 bo dla takich powtórek jak: 111, 222 ... 999. 
bez_zer = 36 * x_do_y(2, n, MOD) - 63 #36 bo 9 po 2, 63 bo 7 * 9. 7 oznacza wielokrotnie naliczone te same kombinacje (111, 222) pomnożone przez 9, bo dla każdej cyfry
print(z_zerem + bez_zer)

########################

import math

def czy_pierwsza(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    
    return True

n = int(input())
if czy_pierwsza(n):
    print("Bartek")
else:
    print("Adam")