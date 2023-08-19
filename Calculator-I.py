# https://py.checkio.org/en/mission/calculator-i/

def dzialaj(akt_w, akt_str, znak):
    if znak == "":
        akt_w = 0
    elif znak == "+":
        k = akt_w
        akt_w = akt_w + int(akt_str)
    else:
        k = akt_w
        akt_w = akt_w - int(akt_str)
    return akt_w


def calculator(log):
    akt_w = -1
    akt_str = ""
    jaki_znak = ""
    czy_byl_juz_int = False
    
    for k in range(len(log)):
        i = log[k]
        if i.isdigit() or (i == "-" and czy_byl_juz_int == False):
            if i.isdigit():
                czy_byl_juz_int = True
            akt_str += i
        else:
            if len(akt_str) != 0:
                if i == "+":
                    if akt_w != -1 and jaki_znak != "":
                        akt_w = dzialaj(akt_w, akt_str, jaki_znak)
                    else:
                        akt_w = int(akt_str)
                    jaki_znak = "+"
                elif i == "-":
                    if akt_w != -1 and jaki_znak != "":
                        akt_w = dzialaj(akt_w, akt_str, jaki_znak)
                    else:
                        akt_w = int(akt_str)
                    jaki_znak = "-"
                else:
                    if akt_w != -1 and jaki_znak != "":
                        akt_w = dzialaj(akt_w, akt_str, jaki_znak)
                    jaki_znak = ""
            akt_str = ""
            
    
    if akt_str != "":
        return str(int(akt_str))
    elif akt_w != -1:
        return str(akt_w)
    else:
        return "0"
                        


print("Example:")
print(calculator('-5-10+15-'))

# These "asserts" are used for self-checking
assert calculator('-5-10+15-') == '0'
assert calculator("000000") == "0"
assert calculator("0000123") == "123"
assert calculator("12") == "12"
assert calculator("+12") == "12"
assert calculator("") == "0"
assert calculator("1+2") == "2"
assert calculator("2+") == "2"
assert calculator("1+2=") == "3"
assert calculator("1+2=2") == "2"
assert calculator("=5=10=15") == "15"
assert calculator("1+2-") == "3"

print("The mission is done! Click 'Check Solution' to earn rewards!")

