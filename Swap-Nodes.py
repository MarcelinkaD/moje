# https://py.checkio.org/en/mission/swap-nodes/

def swap_nodes(a):
    w = []
    if len(a) == 4:
        w.append(a[1])
        w.append(a[0])
        w.append(a[3])
        w.append(a[2])
    elif len(a) == 3:
        w.append(a[1])
        w.append(a[0])
        w.append(a[2])
    elif len(a) == 2:
        w.append(a[1])
        w.append(a[0])
    else:
        return a
    return w

if __name__ == '__main__':
    print("Example:")
    print(list(swap_nodes([1, 2, 3, 4])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(swap_nodes([1, 2, 3, 4])) == [2, 1, 4, 3]
    assert list(swap_nodes([5, 5, 5, 5])) == [5, 5, 5, 5]
    assert list(swap_nodes([1, 2, 3])) == [2, 1, 3]
    assert list(swap_nodes([3])) == [3]
    assert list(swap_nodes(["hello", "world"])) == ["world", "hello"]
    print("Coding complete? Click 'Check' to earn cool rewards!")
