#include <iostream>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int w, l, p, n;
    cin >> w >> l >> p >> n;

    while (l != 0) {
        int pocz = 0;
        int kon = l;

        if (w == (l * n) * -1) {
            cout << 0 << endl;
        } else {
            while (pocz <= kon) {
                int srodek = (pocz + kon) / 2;
                int ile_pkt = srodek * p;
                ile_pkt -= (l - srodek) * n;

                if (ile_pkt == w) {
                    cout << srodek << endl;
                    break;
                } else if (ile_pkt < w) {
                    pocz = srodek + 1;
                } else {
                    kon = srodek;
                }
                }
        }
        cin >> w >> l >> p >> n;
    }




    return 0;
}
