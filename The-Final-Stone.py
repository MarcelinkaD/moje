# https://py.checkio.org/en/mission/the-final-stone/

from heapq import heapify, heappop, heappush

def final_stone(stones):
    l = []
    for i in stones:
        l.append(i * -1)
    
    heapify(l)
    
    while len(l) >= 2:
        a, b = heappop(l), heappop(l)
        reszta = (-1 * min(a, b)) - (-1 * max(a, b))
        
        if reszta != 0:
            heappush(l, -1 * reszta)
            
    if len(l) == 0:
        return 0
    else:
        return -1 * l[0]
        

print('Example:')
print(final_stone([1,2,3]))

assert final_stone([3, 5, 1, 1, 9]) == 1
assert final_stone([1, 2, 3]) == 0
assert final_stone([1, 2, 3, 4]) == 0
assert final_stone([1, 2, 3, 4, 5]) == 1
assert final_stone([1, 1, 1, 1]) == 0
assert final_stone([1, 1, 1]) == 1
assert final_stone([1, 10, 1]) == 8
assert final_stone([1, 10, 1, 8]) == 0
assert final_stone([]) == 0
assert final_stone([1]) == 1
assert final_stone([10, 20, 30, 50, 100, 10, 20, 10]) == 10

print("The mission is done! Click 'Check Solution' to earn rewards!")
