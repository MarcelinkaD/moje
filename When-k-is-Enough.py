# https://py.checkio.org/en/mission/when-k-is-enough/

def remove_after_kth(l, k):
    w = []
    d = {}
    
    for i in l:
        if i not in d:
            d[i] = 0
        d[i] += 1
        
        if d[i] <= k:
            w.append(i)
            
    return w


print("Example:")
print(list(remove_after_kth([42, 42, 42, 42, 42, 42, 42], 3)))

# These "asserts" are used for self-checking
assert list(remove_after_kth([42, 42, 42, 42, 42, 42, 42], 3)) == [42, 42, 42]
assert list(remove_after_kth([42, 42, 42, 99, 99, 17], 0)) == []
assert list(remove_after_kth([1, 1, 1, 2, 2, 2], 5)) == [1, 1, 1, 2, 2, 2]

print("The mission is done! Click 'Check Solution' to earn rewards!")

