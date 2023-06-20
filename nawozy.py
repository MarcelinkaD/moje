# https://szkopul.edu.pl/c/olimpiada-od-podstaw-2022-23/p/nawozy/

from sys import stdin
input = stdin.readline

def main():
    licz_naw, licz_ros = map(int, input().split())
    rosliny = str(input().strip())
    ile_mamy_naw = list(map(int, input().split()))
    ile_mamy_naw.insert(0, 0)
    i = 0
    ile_dow = 0
    akt_licz = ""
    
    while i < licz_ros:
        akt_licz += rosliny[i]
        
        if rosliny[i] == "D":
            if len(akt_licz) == 1:
                ile_dow += 1
            else:
                akt_licz = akt_licz[: len(akt_licz) - 1]
                ile_mamy_naw[int(akt_licz)] -= 1
                
                if ile_mamy_naw[int(akt_licz)] == -1:
                    print("NIE")
                    return
                
                ile_dow += 1
                
            akt_licz = ""
            i += 1
            
        elif int(akt_licz) > licz_naw:
            akt_licz = akt_licz[: len(akt_licz) - 1]
            ile_mamy_naw[int(akt_licz)] -= 1
                
            if ile_mamy_naw[int(akt_licz)] == -1:
                print("NIE")
                return
            
            akt_licz = ""
        
        elif i != licz_ros - 1:
            i += 1
        
        else:
            ile_mamy_naw[int(akt_licz)] -= 1
                
            if ile_mamy_naw[int(akt_licz)] == -1:
                print("NIE")
                return
            
            i += 1
                
        
    if ile_dow == 0:    
        print("TAK")
    else:
        for i in ile_mamy_naw:
            if i != 0:
                ile_dow -= i
            
            if ile_dow <= 0:
                print("TAK")
                return
        
        print("NIE")
    
main()