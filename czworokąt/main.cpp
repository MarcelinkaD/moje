#include <iostream>
using namespace std;

int main()
{
    int q;
    cin >> q;

    for (int i = 0; i < q; i++) {
        int xa, ya;
        cin >> xa >> ya;

        int xb, yb;
        cin >> xb >> yb;

        int xc, yc;
        cin >> xc >> yc;

        int xd, yd;

        // wyznaczanie D na podstawie CD i BA
        int ile_x = max(xa, xb) - min(xa, xb);
        int ile_y = max(ya, yb) - min(ya, yb);

        xd = xc + ile_x;
        yd = yc - ile_y;

        // sprawdzanie AD i BC
        ile_x = max(xa, xd) - min(xa, xd);
        ile_y = max(ya, yd) - min(ya, yd);

        if (yc - ile_y != yc && xc - ile_x != xb) {
            cout << 'NIE' << endl;
        } else {
            cout << xd << ' ' << yd << endl;
        }

    }

    return 0;
}
