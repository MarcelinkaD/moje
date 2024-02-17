#include <iostream>
#include "r3clib.h"

int _x_target, _y_target;
int _queries = 0;
bool _initialized = false;

static void _initialize() {
    if (_initialized)
        return;
    _initialized = true;
    std::cin >> _x_target >> _y_target;
}

int64_t _cross_product(int64_t x1, int64_t y1, int64_t x2, int64_t y2) {
    return x1 * y2 - y1 * x2;
}

int sluchaj(int x1, int y1, int x2, int y2) {
    _initialize();
    _queries += 1;
    auto c = _cross_product(_x_target - x1, _y_target - y1, x2 - x1, y2 - y1);
    if (c == 0)
        return 0;
    return (c < 0 ? -1 : 1);
}

void odpowiedz(int x, int y) {
    _initialize();

    if (_x_target == x && _y_target == y)
        std::cout << "Odnaleziono zrodlo uzywajac " << _queries << " pytan.\n";
    else
        std::cout << "Podano bledne polozenie zrodla (" << x << ", " << y << ").\n";
    exit(0);
}
