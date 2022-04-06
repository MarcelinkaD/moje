from sys import stdin
input = stdin.readline

def main():
    liczba_kwiatow = int(input())
    kwiaty = str(input().strip())
    kwiaty = " " + kwiaty
    liczba_zapytan = int(input())
    sumy_pref_R = [0] * (liczba_kwiatow + 7)
    sumy_pref_N = [0] * (liczba_kwiatow + 7)
    sumy_pref_pary_R_przed_N = [0] * (liczba_kwiatow + 7)
    
    for i in range(1, liczba_kwiatow + 1):
        sumy_pref_N[i] = sumy_pref_N[i - 1]
        if(kwiaty[i] == 'N'):
            sumy_pref_N[i] += 1
    
    for i in range(1, liczba_kwiatow + 1):
        sumy_pref_R[i] = sumy_pref_R[i - 1]
        if(kwiaty[i] == 'R'):
           sumy_pref_R[i] += 1
            
    for i in range(1, liczba_kwiatow + 1):
        sumy_pref_pary_R_przed_N[i] = sumy_pref_pary_R_przed_N[i - 1]
        if kwiaty[i] == "N":
            sumy_pref_pary_R_przed_N[i] = sumy_pref_pary_R_przed_N[i] + sumy_pref_R[i]
    
    for i in range(liczba_zapytan):
        a, b = map(int, input().split())
        index_a = a
        index_b = b
        wynik = 0
        ile_par = sumy_pref_R[index_a - 1] * (sumy_pref_N[index_b] - sumy_pref_N[index_a - 1])
        wynik = sumy_pref_pary_R_przed_N[index_b] - sumy_pref_pary_R_przed_N[index_a - 1] - ile_par
        print(wynik)

main()