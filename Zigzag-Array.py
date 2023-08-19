# https://py.checkio.org/pl/mission/zigzag-array/

def create_zigzag(r, c, start = 1):
    w = [[] for _ in range(r)]
    czy_ros = True
    i = start
    
    for j in range(r):
        if czy_ros:
            for k in range(c):
                w[j].append(i)
                i += 1
            czy_ros = False
            i += c - 1
        else:
            for k in range(i, i - c, -1):
                w[j].append(i)
                i -= 1
            czy_ros = True
            i += c + 1
            
    return w


print("Example:")
print(create_zigzag(3, 5))

# These "asserts" are used for self-checking
assert create_zigzag(3, 5) == [[1, 2, 3, 4, 5], [10, 9, 8, 7, 6], [11, 12, 13, 14, 15]]
assert create_zigzag(5, 1) == [[1], [2], [3], [4], [5]]
assert create_zigzag(3, 3, 5) == [[5, 6, 7], [10, 9, 8], [11, 12, 13]]

print("The mission is done! Click 'Check Solution' to earn rewards!")

