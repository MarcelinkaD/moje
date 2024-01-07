import sys

_x = 0
_y = 0
_moves = 0
_package_picked_up = False
_initialized = False


def _initialize():
    global _x, _y, _x_end, _y_end, _moves, _initialized
    
    if _initialized:
        return
    _initialized = True
    _x_end, _y_end = [int(e) for e in input().split()]


def podnies():
    global _package_picked_up
    _initialize()
    if _package_picked_up:
        print("Wielokrotne wywolanie funkcji podnies.")
        sys.exit(0)
    _package_picked_up = True
    return _x_end, _y_end


def odstaw():
    _initialize()
    if not _package_picked_up:
        print("Wywolano funkcje odstaw nie podnoszac wczesniej paczki.")
        sys.exit(0)
    if _x == _x_end and _y == _y_end:
        print(f"Robocik postawil paczke w dobrym miejscu w {_moves} ruchach.")
    else:
        print(f"Robocik postawil paczke w zlym miejscu ({_x}, {_y}).")
    sys.exit(0)


def do_przodu():
    global _y, _moves
    _initialize()
    if not _package_picked_up:
        print("Wywolano funkcje do_przodu nie podnoszac wczesniej paczki.")
        sys.exit(0)
    _y += 1
    _moves += 1
    print(f"Robocik idzie do przodu ({_x}, {_y}).")

def do_tylu():
    global _y, _moves
    _initialize()
    if not _package_picked_up:
        print("Wywolano funkcje do_tylu nie podnoszac wczesniej paczki.")
        sys.exit(0)
    _y -= 1
    _moves += 1
    print(f"Robocik idzie do tylu ({_x}, {_y}).")

def w_prawo():
    global _x, _moves
    _initialize()
    if not _package_picked_up:
        print("Wywolano funkcje w_prawo nie podnoszac wczesniej paczki.")
        sys.exit(0)
    _x += 1
    _moves += 1
    print(f"Robocik idzie w prawo ({_x}, {_y}).")

def w_lewo():
    global _x, _moves
    _initialize()
    if not _package_picked_up:
        print("Wywolano funkcje w_lewo nie podnoszac wczesniej paczki.")
        sys.exit(0)
    _x -= 1
    _moves += 1
    print(f"Robocik idzie w lewo ({_x}, {_y}).")
