# https://py.checkio.org/en/mission/the-fastest-horse/

def fastest_horse(h):
    w = [0 for _ in range(len(h[0]))]
    
    for i in range(len(h)):
        naj = h[i][0]
        ind = 0
        for k in range(1, len(h[i])):
            if int(h[i][k][0]) <= int(naj[0]):
                min1 = h[i][k][2 : 4]
                min2 = naj[2 : 4]
                if min1.isdigit() and min2.isdigit():
                    if int(min1) < int(min2):
                        naj = h[i][k]
                        ind = k
                else:
                    if min1.isdigit():
                        min1 = int(min1)
                        min2 = int(min2[1])
                    else:
                        min1 = int(min1[1])
                        min2 = int(min2)
                    if int(min1) < int(min2):
                        naj = i[i]
                        ind = i
        w[ind] += 1
        
    maxi = -1
    ind = 0
    
    for i in range(len(w)):
        if w[i] > maxi:
            maxi = w[i]
            ind = i + 1
            
    return ind

if __name__ == '__main__':
    print("Example:")
    print(fastest_horse([['1:13', '1:26', '1:11'], ['1:10', '1:18', '1:14'], ['1:20', '1:23', '1:15']]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert fastest_horse([['1:13', '1:26', '1:11'], ['1:10', '1:18', '1:14'], ['1:20', '1:23', '1:15']]) == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")