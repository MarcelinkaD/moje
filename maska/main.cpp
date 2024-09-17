#include <iostream>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int y, x, z;
    cin >> y >> x >> z;

    int max_var = max(max(y, x), z);

    if (max_var == y) {
        if (x > z) {
            cout << (x / 2);
        } else {
            cout << (z / 2);
        }
    } else if (max_var == x) {
        if (y > z) {
            cout << (y / 2);
        } else {
            cout << (z / 2);
        }
    } else {
        if (x > y) {
            cout << (x / 2);
        } else {
            cout << (y / 2);
        }
    }

    return 0;
}
