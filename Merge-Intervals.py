# https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/803/

def czy_sie_pokrywa(l1, l2):
    if l1[1] >= l2[0] or (l1[0] >= l2[0] and l1[1] >= l2[1]):
        return [min(l1[0], l2[0]), max(l1[1], l2[1])]
    else:
        return False
    
def merge(l):
    if len(l) == 1:
        return l
    
    w = []
    l = sorted(l)
    akt_w = l[0]
    
    for i in range(1, len(l)):
        odp = czy_sie_pokrywa(akt_w, l[i])
        if odp != False:
            akt_w = odp
            
            if i == len(l) - 1:
                w.append(akt_w)
                
        else:
            w.append(akt_w)
            akt_w = l[i]
            
            if i == len(l) - 1:
                w.append(l[i])
    
    return w

print(merge([[1,4],[4,5]]))