//Podzielne
/*#include <iostream>
#define ll long long
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    ll a, b;
    cin >> a >> b;

    ll p3 = (b / 3) - ((a - 1) / 3);
    ll p5 = (b / 5) - ((a - 1) / 5);
    ll p15 = (b / 15) - ((a - 1) / 15);

    cout << (p3 + p5) - p15;

    return 0;
}
*/

//Choinka 2
/*
#include <iostream>
using namespace std;

void rysuj_choinke(int n) {
    int akt_spa = n;
    int akt_gwia = 1;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < akt_spa; j++) {
            cout << ' ';
        }
        for (int j = 0; j < akt_gwia; j++) {
            cout << '*';
        }
        for (int j = 0; j < akt_spa; j++) {
            cout << ' ';
        }
        cout << endl;
        akt_spa--;
        akt_gwia += 2;
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;
    rysuj_choinke(n);
    rysuj_choinke(n);

    for (int j = 0; j < (2 * n + 1); j++) {
        cout << '*';
    }

    return 0;
}
*/

//Wezyk
/*
#include <iostream>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;
    int licz = 1;

    for (int i = 0; i < n; i++) {
        if (i % 2 == 0) {
            for (int k = 0; k < n; k++) {
                cout << licz << ' ';
                licz++;
            }
        } else {
            licz += n - 1;
            for (int k = 0; k < n; k++) {
                cout << licz << ' ';
                licz--;
            }
            licz += n + 1;
        }
        cout << endl;
    }

    return 0;
}
*/

//Sciezka Sterna-Brocota
#include <iostream>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    double a, b;
    cin >> a >> b;

    double lx = 0, ly = 1;
    double px = 1, py = 0;
    double ul = a / b;

    while (2 + 2 == 4){
        double nx = lx + px, ny = ly + py;

        if (nx == a && ny == b) {
            break;
        }

        if (ul < nx / ny) {
            px = nx;
            py = ny;
            cout << 'L';
        } else {
            lx = nx;
            ly = ny;
            cout << 'P';
        }

    }

    return 0;
}


//Przenoszenie
/*#include <iostream>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int q;
    cin >> q;

    for (int i = 0; i < q; i++) {
        long long a, b, w = 0;
        cin >> a >> b;
        int ola, olb, akt_prze = 0;

        while (min(a, b) > 0) {
            ola = a % 10;
            olb = b % 10;
            akt_prze = (ola + olb + akt_prze) / 10;
            if (akt_prze > 0) {
                w++;
            }
            a /= 10;
            b /= 10;
        }

        if (akt_prze > 0) {
            if (a == 0) {
                while (b > 0) {
                    olb = b % 10;
                    akt_prze = (olb + akt_prze) / 10;
                    if (akt_prze > 0) {
                        w++;
                    }
                    b /= 10;
                }
            } else {
                while (a > 0) {
                    ola = a % 10;
                    akt_prze = (ola + akt_prze) / 10;
                    if (akt_prze > 0) {
                        w++;
                    }
                    a /= 10;
                }
            }
        }
        cout << w << endl;
    }

    return 0;
}
*/
