# https://py.checkio.org/en/mission/largest-histogram/

import bisect as bi

def czy_da_sie1(x, his):
    w = 0
    max_w = 0
    for i in range(len(his)):
        if his[i] < x:
            max_w = max(w, max_w)
            w = 0 
        else:
            w += 1
    
    max_w = max(w, max_w)
    
    return max_w

def czy_da_sie2(x, his):
    w = 0
    
    if len(his) >= x:
        w = min(his)
    
    return w
    
def czy_da_sie(x, his):
    w1 = czy_da_sie1(x, his) * x
    w2 = czy_da_sie2(x, his) * x
    
    return max(w1, w2)
    
def largest_histogram(his):
    pocz = 1
    kon = len(his)
    naj_w = max(his)
    
    for srodek in range(pocz, kon + 1):
        co_mamy = czy_da_sie(srodek, his)
        if co_mamy != 0:
            naj_w = max(naj_w, co_mamy)
            
    return naj_w


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert largest_histogram([5]) == 5, "one is always the biggest"
    assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    assert largest_histogram([1, 2, 3, 2, 1]) == 6, "nowe"
    print("Done! Go check it!")

