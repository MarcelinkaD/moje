# https://py.checkio.org/pl/mission/reveal-the-number/

def reveal_num(line):
    w = ""
    czy_plus = True
    czy_byla_liczba = False
    czy_byla_juz_kropka = False
    for i in range(len(line)):
        if line[i] == "-" or line[i] == "+":
            if czy_byla_liczba == False:
                if line[i] == "-":
                    czy_plus = False
                else:
                    czy_plus = True            
        elif line[i] == ".":
            if czy_byla_juz_kropka == False:
                czy_byla_juz_kropka = True
                w += "."
        else:
            if line[i].isdigit():
                w += line[i]
                czy_byla_liczba = True
                
    if len(w) == 0:
        return None
    
    if czy_byla_juz_kropka:
        w = float(w)
    else:
        w = int(w)

    if czy_plus == False:
        w *= -1
        
    return w

print("Example:")
print(reveal_num("+A%+-1-0..."))

# These "asserts" are used for self-checking
assert reveal_num("F0(t}") == 0
assert reveal_num("Utc&g") == None
assert reveal_num("-aB%|_-+2ADS.12+3.ADS1.2") == 2.12312
assert reveal_num("-aB%|_+-2ADS.12+3.ADS1.2") == -2.12312
assert reveal_num("zV№1}3;o.vEf``C.WqTY0") == 13.0
assert reveal_num("!3B'j=(}89JQ6aWvN*%5@uy.r)B<?pZ.!545ZD^KF9Sx@gqfa*") == 38965.5459

print("The mission is done! Click 'Check Solution' to earn rewards!")

