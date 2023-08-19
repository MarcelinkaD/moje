# https://py.checkio.org/pl/mission/long-non-repeat/

def non_repeat(line):
    if len(line) < 2:
        return line
    
    w = ""
    maxw = -1
    max_winn = ""
    akt_w = 0
    dic = {line[0] : 0}
    glowa = -1
    ogon = 0
    n = len(line)
    
    while ogon < n - 1:
        while glowa < n - 1 and max(dic.values()) <= 1:
            glowa += 1
            akt_w += 1
            w += line[glowa]
            
            if line[glowa] not in dic:
                dic[line[glowa]] = 0
                
            dic[line[glowa]] += 1
            
            if max(dic.values()) <= 1 and maxw < akt_w:
                maxw = max(maxw, akt_w)
                max_winn = w
            

        akt_w -= 1
        dic[line[ogon]] -= 1
        ogon += 1
        w = w[1:]
        
        if max(dic.values()) <= 1 and maxw < akt_w:
            maxw = max(maxw, akt_w)
            max_winn = w
            
    return max_winn
        
            


print("Example:")
print(non_repeat(""))

# These "asserts" are used for self-checking
assert non_repeat('') == ''
assert non_repeat("aaaaa") == "a"
assert non_repeat("abdjwawk") == "abdjw"
assert non_repeat("abcabcffab") == "abcf"

print("The mission is done! Click 'Check Solution' to earn rewards!")


