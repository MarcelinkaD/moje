//https://szkopul.edu.pl/c/map-2024_2025/p/pli/

#include <iostream>
#include <math.h>
using namespace std;

int odw(int x) {
    int pal = 0;

    while (x > 0) {
        pal += x % 10;
        x /= 10;
        if (x > 0) {
            pal *= 10;
        }
    }
    return pal;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n, w;
    cin >> n;

    int pal = odw(n);

    if (pal == n) {
        cout << 0 << endl;
        return 0;
    }

    int x = n;
    while (2 + 2 == 4) {
        x++;
        if (odw(x) == x) {
            cout << x - n;
            return 0;
        }
    }

    return 0;
}
