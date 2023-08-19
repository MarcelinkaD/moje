# https://py.checkio.org/en/mission/find-sequence/

def cds1(matrix, y, x):
    if y + 3 < len(matrix):
        if matrix[y + 1][x] == matrix[y][x] and matrix[y + 2][x] == matrix[y][x] and matrix[y + 3][x] == matrix[y][x]:
            return True
    return False

def cds2(matrix, y, x):
    if x + 3 < len(matrix[0]):
        if matrix[y][x + 1] == matrix[y][x] and matrix[y][x + 2] == matrix[y][x] and matrix[y][x + 3] == matrix[y][x]:
            return True
    return False

def cds3(matrix, y, x):
    if x + 3 < len(matrix[0]) and y + 3 < len(matrix):
        if matrix[y + 1][x + 1] == matrix[y][x] and matrix[y + 2][x + 2] == matrix[y][x] and matrix[y + 3][x + 3] == matrix[y][x]:
            return True
    return False

def cds4(matrix, y, x):
    if x + 3 < len(matrix[0]) and y - 3 > -1:
        if matrix[y - 1][x + 1] == matrix[y][x] and matrix[y - 2][x + 2] == matrix[y][x] and matrix[y - 3][x + 3] == matrix[y][x]:
            return True
    return False

def checkio(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
    for i in range(n):
        for k in range(m):
            if cds1(matrix, i, k):
                return True
            elif cds2(matrix, i, k):
                return True
            elif cds3(matrix, i, k):
                return True
            elif cds4(matrix, i, k):
                return True
    
    return False

print("Example:")
print(checkio([[1, 2, 1, 1], [1, 1, 4, 1], [1, 3, 1, 6], [1, 7, 2, 5]]))

# These "asserts" are used for self-checking
assert checkio([[1, 2, 1, 1], [1, 1, 4, 1], [1, 3, 1, 6], [1, 7, 2, 5]]) == True
assert checkio([[7, 1, 4, 1], [1, 2, 5, 2], [3, 4, 1, 3], [1, 1, 8, 1]]) == False
assert (
    checkio(
        [
            [2, 1, 1, 6, 1],
            [1, 3, 2, 1, 1],
            [4, 1, 1, 3, 1],
            [5, 5, 5, 5, 5],
            [1, 1, 3, 1, 1],
        ]
    )
    == True
)
assert (
    checkio(
        [
            [7, 1, 1, 8, 1, 1],
            [1, 1, 7, 3, 1, 5],
            [2, 3, 1, 2, 5, 1],
            [1, 1, 1, 5, 1, 4],
            [4, 6, 5, 1, 3, 1],
            [1, 1, 9, 1, 2, 1],
        ]
    )
    == True
)
assert (
    checkio(
        [
            [2, 6, 2, 2, 7, 6, 5],
            [3, 4, 8, 7, 7, 3, 6],
            [6, 7, 3, 1, 2, 4, 1],
            [2, 5, 7, 6, 3, 2, 2],
            [3, 4, 3, 2, 7, 5, 6],
            [8, 4, 6, 5, 2, 9, 7],
            [5, 8, 3, 1, 3, 7, 8],
        ]
    )
    == False
)
assert (
    checkio(
        [
            [1, 7, 6, 1, 8, 5, 1],
            [7, 9, 1, 7, 2, 8, 6],
            [5, 1, 4, 5, 8, 8, 3],
            [8, 6, 3, 9, 7, 6, 9],
            [9, 8, 9, 8, 6, 8, 2],
            [1, 7, 2, 4, 9, 3, 8],
            [9, 9, 8, 6, 9, 2, 6],
        ]
    )
    == False
)
assert (
    checkio(
        [
            [6, 9, 1, 1, 6, 2],
            [5, 9, 7, 8, 2, 5],
            [2, 1, 1, 7, 9, 8],
            [1, 8, 1, 4, 7, 4],
            [7, 8, 5, 4, 5, 1],
            [6, 4, 8, 8, 1, 8],
        ]
    )
    == False
)
assert (
    checkio(
        [
            [2, 7, 6, 2, 1, 5, 2, 8, 4, 4],
            [8, 7, 5, 8, 9, 2, 8, 9, 5, 5],
            [5, 7, 7, 7, 4, 1, 1, 2, 6, 8],
            [4, 6, 6, 3, 2, 7, 6, 6, 5, 1],
            [2, 6, 6, 9, 8, 5, 5, 6, 7, 7],
            [9, 4, 1, 9, 1, 3, 7, 2, 3, 1],
            [5, 1, 4, 3, 6, 5, 9, 3, 4, 1],
            [6, 5, 5, 1, 7, 7, 8, 2, 1, 1],
            [9, 5, 7, 8, 2, 9, 2, 6, 9, 3],
            [8, 2, 5, 7, 3, 7, 3, 8, 6, 2],
        ]
    )
    == False
)
assert (
    checkio(
        [
            [1, 9, 7, 8, 9, 3, 6, 5, 6, 2],
            [4, 9, 4, 8, 3, 4, 8, 8, 5, 9],
            [2, 8, 5, 5, 7, 8, 6, 1, 3, 6],
            [6, 4, 7, 6, 9, 1, 4, 5, 7, 8],
            [4, 7, 7, 9, 8, 8, 8, 8, 4, 4],
            [3, 7, 3, 2, 1, 9, 1, 8, 9, 1],
            [4, 7, 2, 4, 8, 1, 2, 3, 6, 2],
            [4, 4, 1, 3, 3, 3, 9, 2, 6, 7],
            [8, 6, 1, 9, 3, 5, 8, 1, 7, 5],
            [7, 3, 6, 5, 3, 6, 6, 4, 8, 2],
        ]
    )
    == True
)
assert checkio([[1, 6, 1, 7], [4, 7, 3, 6], [3, 5, 7, 9], [8, 6, 6, 9]]) == False
assert (
    checkio(
        [
            [1, 2, 4, 6, 3],
            [2, 5, 2, 6, 3],
            [8, 7, 5, 9, 5],
            [2, 1, 1, 4, 3],
            [4, 2, 7, 5, 1],
        ]
    )
    == False
)
assert (
    checkio(
        [
            [2, 3, 6, 5, 6, 2, 8, 3, 7, 4],
            [6, 9, 5, 9, 7, 6, 8, 5, 1, 6],
            [6, 8, 2, 6, 1, 9, 3, 6, 6, 4],
            [5, 8, 3, 2, 3, 8, 7, 4, 6, 4],
            [2, 3, 1, 4, 5, 1, 2, 5, 6, 9],
            [5, 4, 8, 7, 5, 5, 8, 4, 9, 5],
            [9, 7, 9, 9, 5, 9, 9, 8, 1, 2],
            [5, 1, 7, 4, 8, 3, 4, 1, 8, 8],
            [5, 3, 3, 2, 6, 1, 4, 3, 8, 8],
            [4, 8, 1, 4, 5, 8, 8, 7, 4, 7],
        ]
    )
    == True
)
assert (
    checkio(
        [
            [7, 7, 4, 4, 8],
            [7, 4, 5, 5, 6],
            [6, 6, 5, 2, 8],
            [6, 2, 3, 8, 4],
            [6, 1, 3, 1, 2],
        ]
    )
    == False
)
assert (
    checkio(
        [
            [7, 9, 1, 7, 6, 7, 5, 9, 6],
            [5, 5, 9, 3, 1, 6, 7, 4, 7],
            [1, 7, 5, 2, 3, 1, 6, 4, 7],
            [2, 2, 2, 8, 7, 2, 6, 6, 9],
            [5, 6, 4, 2, 6, 7, 3, 4, 7],
            [5, 5, 6, 4, 9, 4, 3, 1, 7],
            [7, 3, 2, 3, 2, 4, 4, 7, 3],
            [3, 6, 9, 7, 2, 5, 6, 2, 5],
            [4, 1, 3, 9, 4, 2, 4, 8, 4],
        ]
    )
    == True
)

print("The mission is done! Click 'Check Solution' to earn rewards!")

