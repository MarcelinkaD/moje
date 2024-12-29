// 2) https://cses.fi/problemset/task/1648/
#include <iostream>
#include <vector>
#define ll long long
using namespace std;

const int R = (1 << 18);
ll drzewo[2 * R];

void zamien(int k, int u) {
    k += R;
    drzewo[k] = u;

    while(k > 1) {
        k /= 2;
        drzewo[k] = drzewo[2 * k] + drzewo[2 * k + 1];
    }
}

ll suma(int pocz, int kon) {
    pocz += R;
    kon += R;

    if (pocz == kon) {
        return drzewo[pocz];
    }

    ll w = drzewo[pocz] + drzewo[kon];

    while (pocz != kon - 1) {
        if (pocz % 2 == 0) {
            w += drzewo[pocz + 1];
        }
        if (kon % 2 == 1) {
            w += drzewo[kon - 1];
        }

        pocz /= 2;
        kon /= 2;
    }
    return w;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n, q;
    cin >> n >> q;

    for (int i = 1; i <= n; i++) {
        cin >> drzewo[i + R];
    }

    for (int i = R - 1; i >= 1; i--) {
        drzewo[i] = drzewo[2 * i] + drzewo[2 * i + 1];
    }

    for (int i = 0; i < q; i++) {
        int rodzaj;
        cin >> rodzaj;
        if (rodzaj == 1) {
            int k, u;
            cin >> k >> u;
            zamien(k, u);
        } else {
            int pocz, kon;
            cin >> pocz >> kon;
            cout << suma(pocz, kon) << endl;
        }
    }

    return 0;
}
