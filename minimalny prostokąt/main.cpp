#include <iostream>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;

    int maxx = -10000;
    int maxy = -10000;
    int minx = 10000;
    int miny = 10000;

    for (int i = 0; i < n; i++) {
        int x, y;
        cin >> x;
        cin >> y;

        maxx = max(x, maxx);
        minx = min(x, minx);
        maxy = max(y, maxy);
        miny = min(y, miny);
    }

    int a = maxx - minx;
    int b = maxy - miny;

    if (a == 0) {
        a = 1;
    }

    if (b == 0) {
        b = 1;
    }

    cout << a * b;


    return 0;
}
