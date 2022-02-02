from sys import setrecursionlimit
setrecursionlimit(1000000)

licznik = 1

def DFS(wie1, wie2, graf, pre, post):
    global licznik
    pre[wie1] = licznik
    licznik += 1
    
    for sasiad in graf[wie1]:
        if(sasiad != wie2):
            DFS(sasiad, wie1, graf, pre, post)
    
    post[wie1] = licznik
    licznik += 1
    
def czy_szef(w1, w2, pre, post):
    return (pre[w1] < pre[w2]) and (post[w1] > post[w2])

def main():
    liczba_wieszcholkow, liczba_zapytan = map(int, input().split())
    graf = [[] for i in range(liczba_wieszcholkow + 1)]
    wierzcholki = list(map(int, input().split()))
    
    for i in range(liczba_wieszcholkow - 1):
            graf[i + 2].append(wierzcholki[i])
            graf[wierzcholki[i]].append(i + 2)
        
    pre = [0] * (liczba_wieszcholkow + 1)
    post = [0] * (liczba_wieszcholkow + 1)
    DFS(1, 1, graf, pre, post)
    
    for i in range(liczba_zapytan):
        pierwszy, drugi, ten_co_sie_nie_zgadza = map(int, input().split())
        konflikt1 = czy_szef(ten_co_sie_nie_zgadza, pierwszy, pre, post)
        konflikt2 = czy_szef(ten_co_sie_nie_zgadza, drugi, pre, post)
        
        if(ten_co_sie_nie_zgadza == 1):
            print("Dyrektor patrzy")
        elif(konflikt1 and konflikt2):
            print("Dyrektor patrzy")
        elif(konflikt1):
            print("Tylko B")
        elif(konflikt2):
            print("Tylko A")
        else:
            print("Droga wolna")
    
main()