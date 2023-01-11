from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    wyr = [str(input()).strip() for _ in range(n)]
    miejsce = [0 for _ in range(n)]
    alfa = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    alfa = sorted(alfa, reverse = True)
    
    w = ""
    
    for c in alfa:
        mini = 10000007
        for i in range(len(wyr)):
            akt_zlicz = 0
            for k in range(miejsce[i], len(wyr[i])):
                if wyr[i][k] == c:
                    akt_zlicz += 1
                
            mini = min(mini, akt_zlicz)
            
        w += c * mini
        
        if mini != 0:
            for i in range(n):
                z = 0
                for k in range(miejsce[i], len(wyr[i])):
                    if wyr[i][k] == c:
                        z += 1
                    if z == mini:
                        miejsce[i] = k
                        break
                    
            
    
    print(max(w,"bitek"))
    
main()
