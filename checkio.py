import queue as q

def znajdz_somsiadow(x, l):
    x = str(x)
    w = []
    for i in l:
        if i == int(x):
            continue
        else:
            i = str(i)
            wyn = 0
            for k in range(len(str(i))):
                if i[k] == x[k]:
                    wyn += 1
                    
            if wyn == 2:
                w.append(int(i))
                
    return w


from collections import deque

def bfs(graph, start, end):
    queue = deque([[start]])
    visited = set([start])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == end:
            return path

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])

    return None

    
    
def checkio(num):
    pie = num[0]
    ost = num[-1]
    graf = {}
    
    for i in num:
        wszyscy_somsiedzi = znajdz_somsiadow(i, num)
        graf[i] = wszyscy_somsiedzi
    
    return bfs(graf, pie, ost)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([123, 991, 323, 321, 329, 121, 921, 125, 999]) == [123, 121, 921, 991, 999], "First"
    assert checkio([111, 222, 333, 444, 555, 666, 121, 727, 127, 777]) == [111, 121, 127, 727, 777], "Second"
    assert checkio([456, 455, 454, 356, 656, 654]) == [456, 454, 654], "Third, [456, 656, 654] is correct too"


