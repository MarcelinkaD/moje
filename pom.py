from sys import stdin
input = stdin.readline

def main():
    pomiar = ""
    osoby = 0

    while pomiar != -1:
        poprzedni_pomiar = pomiar
        pomiar = int(input())

        if(pomiar == -1):
            break

        if(pomiar != poprzedni_pomiar and poprzedni_pomiar != ""):
            osoby += 1

    print(osoby)

main()