n=int(input())

wisnie = input().split()
 
pref1=[0] * (n+1)
for indeks in range(0,n):        
    pref1[indeks]=int(wisnie[indeks])+pref1[indeks-1]
        
liczbaPytan=int(input())
for pytanie in range(liczbaPytan):
    od,do = map(int, input().split())
    print(pref1[do-1] - pref1[od-1-1])

