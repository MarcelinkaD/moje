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
print(x_do_y(9, n, int(1e9)))

########################################################

def x_do_y(x, y, MOD):
    if y == 0:
        return 1
    else:
        if y % 2 == 1:
            return x * x_do_y(x, y - 1, MOD) % MOD
        else:
            pol = x_do_y(x, y // 2, MOD)
            return pol * pol % MOD

x, y = map(int, input().split())
suma = (y * (y + 1)) // 2
print(x_do_y(x, suma, int(1e9)))

########################################################

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
do_ile = (n - 2) + 1
print(45 * x_do_y(2, do_ile, int(1e9)))









