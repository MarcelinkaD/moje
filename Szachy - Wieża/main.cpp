#include <iostream>

using namespace std;

int main()
{
    int sx, sy;
    cin >> sx >> sy;
    int kx, ky;
    cin >> kx >> ky;

    if ((sx == kx || sy == ky) && !(sx == kx && sy == ky)) {
        cout << "TAK";
    } else {
        cout << "NIE";
    }

    return 0;
}
