# https://py.checkio.org/en/mission/create-intervals/

def create_intervals(data):
    data = sorted(list(data))
    
    if len(data) == 0:
        return []
    
    akt = [data[0]]
    w = []
    
    for i in range(1, len(data)):
        if data[i - 1] + 1 == data[i]:
            akt.append(data[i])
        else:
            if len(akt) == 1:
                w.append((akt[0], akt[0]))
            else:
                k = (akt[0], akt[-1])
                w.append(k)
            akt = [data[i]]
    
    if len(akt) != 0:
        if len(akt) == 1:
            w.append((akt[0], akt[0]))
        else:
            k = (akt[0], akt[-1])
            w.append(k)
            
    return w

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)], "First"
    assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"
    assert create_intervals([]) == [], "third"
    print('Almost done! The only thing left to do is to Check it!')

