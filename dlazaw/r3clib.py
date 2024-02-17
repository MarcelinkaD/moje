import sys

_x_target = 0
_y_target = 0
_queries = 0
_initialized = False


def _initialize():
    global _x_target, _y_target, _initialized

    if _initialized:
        return
    _initialized = True
    _x_target, _y_target = [int(e) for e in input().split()]


def _cross_product(x1, y1, x2, y2):
    return x1 * y2 - y1 * x2


def sluchaj(x1, y1, x2, y2):
    global _queries
    _initialize()
    _queries += 1
    c = _cross_product(_x_target - x1, _y_target - y1, x2 - x1, y2 - y1)
    if c == 0:
        return 0
    return -1 if c < 0 else 1


def odpowiedz(x, y):
    _initialize()

    if _x_target == x and _y_target == y:
        print(f"Odnaleziono zrodlo uzywajac {_queries} pytan.")
    else:
        print(f"Podano bledne polozenie zrodla ({x}, {y}).")
    sys.exit(0)
