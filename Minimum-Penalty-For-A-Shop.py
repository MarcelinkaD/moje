# https://leetcode.com/problems/minimum-penalty-for-a-shop/
    
def main(s):
    if s == "YN":
        return 1
    
    w = -1
    mini = 1e10
    pref_y = [0] * len(s)
    pref_n = [0] * len(s)
    
    if pref_n[0] == "N":
        pref_n[0] = 1
        
    if pref_y[0] == "Y":
        pref_y[0] = 1
    
    for i in range(1, len(s)):
        pref_n[i] = pref_n[i - 1]
        pref_y[i] = pref_y[i - 1]
        
        if s[i] == "N":
            pref_n[i] += 1
        else:
            pref_y[i] += 1
    
    for i in range(len(s) + 1):
        akt_w = 0
        if i != len(s):
            akt_w += pref_n[max(0, i - 1)]
            akt_w += pref_y[-1] - pref_y[max(0, i - 1)]
            
            if mini > akt_w:
                mini = akt_w
                w = i
        else:
            akt_w += pref_n[-1]
                    
            if mini > akt_w:
                mini = akt_w
                w = i
    
    return w

print(main("YYYY"))