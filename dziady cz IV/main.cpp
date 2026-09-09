#include <bits/stdc++.h>
typedef double D;
using namespace std;

D W(D x, D a5, D a4, D a3, D a2, D a1, D a0){
    return (a5 * (x * x * x * x * x)) + (a4 * (x * x * x * x)) + (a3 * (x * x * x)) + (a2 * (x * x)) + (a1 * x) + a0;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    D a5, a4, a3, a2, a1, a0;
    cin >> a5 >> a4 >> a3 >> a2 >> a1 >> a0;

    D pocz = -10;
    D kon = 10;
    if (W(pocz, a5, a4, a3, a2, a1, a0) < 0){
        kon = -10;
        pocz = 10;
    }
    int k = 40;
    while (k--){
        D srodek = (pocz + kon) / 2;
        D wyn_srodek = W(srodek, a5, a4, a3, a2, a1, a0);
        if (wyn_srodek < 0){
            kon = srodek;
        } else {
            pocz = srodek;
        }
    }

    cout << fixed << setprecision(30);
    cout << pocz << endl;

    return 0;
}
