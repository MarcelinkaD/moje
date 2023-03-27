def brut(n, l):
    max_wyn = 0
    
    for i in range(n):
        w = 0
        czy_ros = True
        for k in range(i + 1, n):
            if l[k - 1] < l[k] and czy_ros:
                w += 1
            elif l[k - 1] > l[k] and czy_ros:
                w += 1
                czy_ros = False
            elif l[k - 1] > l[k] and czy_ros == False:
                w += 1
            elif l[k - 1] < l[k] and czy_ros == False:
                break
        
        max_wyn = max(max_wyn, w + 1)
        
    return max_wyn

def fast(n, l):
    max_wyn = 0
    
    for i in range(n):
        w = 0
        czy_ros = True
        for k in range(i + 1, n):
            if l[k - 1] < l[k] and czy_ros:
                w += 1
            elif l[k - 1] > l[k] and czy_ros:
                w += 1
                czy_ros = False
            elif l[k - 1] > l[k] and czy_ros == False:
                w += 1
            elif l[k - 1] < l[k] and czy_ros == False:
                break
        
        max_wyn = max(max_wyn, w + 1)
        
    return max_wyn




import random

numer_testu = 1
while True:
    n = random.randint(1, 10)
    a = [0 for i in range(n)]
    for i in range(n):
        a[i] = random.randint(1, 20)
    
    [wynik1, wynik2] = [brut(n, a), fast(n, a)]
    if wynik1 == wynik2:
        print("Test " + str(numer_testu) + "     " + str(wynik1))
        print("\nwejscie:")
        print(n)
        for i in range(n):
            print(a[i], end = ' ')
        print("\n")
    else:
        print("Test " + str(numer_testu) + "     ZLA ODPOWIEDZ")
        print("\nwejscie:")
        print(n)
        for i in range(n):
            print(a[i], end = ' ')
        print("\n\nwynik bruta:         " + str(wynik1))
        print("\nwynik wzorcowki:     " + str(wynik2))
        
        break
    
    numer_testu += 1
