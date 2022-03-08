#Ważne rzeczy:
# - odległość[1, 2] = abs(x1 - x2) + abs(y1 - y2)
# - to GRAF!! z wagami

wierzcholki =  [[0,0], [2,2], [3,10], [5,2], [7,0]]
reprezentanci = [i for i in range(len(wierzcholki))]
kraw = []

def Find(v):
    global reprezentanci
    if(reprezentanci[v] == v):
        return v
    else:
        k = Find(reprezentanci[v])
        reprezentanci[v] = k
        return k
        
def Union(u, v):
    global reprezentanci    
    a = Find(u)
    b = Find(v)
    reprezentanci[a] = b
        
def main():                                                             

    global wierzcholki
    global reprezentanci
    global kraw
    
    for i in range(len(wierzcholki)):
        for k in range(i + 1, len(wierzcholki)):
            d = abs(wierzcholki[i][0] - wierzcholki[k][0]) + abs(wierzcholki[i][1] - wierzcholki[k][1])
            kraw.append([d, i, k])
    
    kraw.sort()
    wynik = 0
    
    for d, u, v in kraw:
        if (Find(u) != Find(v)):
            wynik += d
            Union(u, v)
    print(wynik)
    

main()
 
 
