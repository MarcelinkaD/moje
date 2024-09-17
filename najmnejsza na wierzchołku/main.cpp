#include <iostream>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int a, b, c;
    cin >> a >> b >> c;

    int x = ((c - (a + b)) * -1) / 2;
    int y = b - x;
    int z = a - x;

    if (x <= y && x <= z) {
        cout << x;
    } else if (y <= x && y <= z) {
        cout << y;
    } else {
        cout << z;
    }

    return 0;
}
