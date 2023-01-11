from sys import stdin
input = stdin.readline

def main():
    n, mod = map(int, input().split())
    l = str(input().strip())
    w = [0 for _ in range(n)]
    w[0] = 1

    for i in range(1, n):
        if l[i] == "0":
            w[i] = 0
        else:
            for k in range(max(0, i - 6), i):
                w[i] += int(w[k])
                
            w[i] %= mod
                
            

    print(w[n - 1])


main()
