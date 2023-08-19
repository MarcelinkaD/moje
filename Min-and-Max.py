# https://py.checkio.org/en/mission/min-max/

def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

def min(*args, **kwargs):
    key = kwargs.get("key", None)
    if len(args) == 1:
        args = args[0]
    argLista = list(args)
    w = argLista[0]
    if key == None:
        for i in argLista:
            if i < w:
                w = i
    else:
        for i in args:
            if key(i) < key(w):
                w = i
    
    return w
    
   

def max(*args, **kwargs):
    key = kwargs.get("key", None)
    if len(args) == 1:
        args = args[0]
    argLista = list(args)
    w = argLista[0]
    if key == None:
        for i in argLista:
            if i > w:
                w = i
        return w
    else:
        for i in args:
            if key(i) > key(w):
                w = i
    
    return w


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert min(abs(i) for i in range(-10, 10)) == 0, "Simple case mins"
    assert min(set('djsaljldsklfjzx')) == "a", "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")


