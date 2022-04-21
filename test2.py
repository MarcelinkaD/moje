def oddSum():
    plik_z_ciagami = open("ciagi.txt", "r+")
    plik_z_wynikami = open("wynik.txt", "w+")
    
    for i in plik_z_ciagami:
        w = 0
        for k in i.split():
            if int(k) % 2 == 1:
                w += int(k)
        
        if w == int(i.split()[0]):
            plik_z_wynikami.write(i)
            
    plik_z_ciagami.close()
    plik_z_wynikami.close()
    
    
oddSum()