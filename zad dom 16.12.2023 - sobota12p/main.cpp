/*
// 1) Implementacja zadania nr 2 (ile par z 0 na koñcu?)
#include <iostream>
using namespace std;

int main()
{
    int przez10 = 0, przez5 = 0, przez2 = 0, przeznic = 0;
    int n;
    cin >> n;

    for (int i = 0; i < n; i++){
        int x;
        cin >> x;

        if (x % 10) {
            przez10++;
        } else if (x % 5 == 0) {
            przez5++;
        } else if (x % 2 == 0) {
            przez2++;
        } else {
            przeznic++;
        }
    }

    int wynik = (przez10 * (przez5 + przez2 + przeznic) + przez5 * przez2 + przez10 * (przez10 - 1)) / 2;

    cout << wynik;

    return 0;
}
*/

/*
// 2) Implementacja zadania nr 3 (ile zer na koñcu ma silnia)
#include <iostream>
using namespace std;

int main() {
    long long n, w = 0;
    cin >> n;

    for(long long pot = 5; pot <= n; pot *= 5) {
        w += n / pot;
    }

    cout << w;

    return 0;
}
*/

// 4) Implementacja zadania nr 5
#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<pair<int, int>> licz5i2;
    licz5i2.push_back({0, 0});
    int akt_piat = 0, akt_dwo = 0;

    for (int i = 0; i < n; i++){
        int x;
        cin >> x;
        while (x % 5 == 0) {
            akt_piat++;
            x /= 5;
        }
        if (x % 2 == 0) {
            akt_dwo++;
            x /= 2;
        }

        licz5i2.push_back({akt_piat, akt_dwo});
    }

    int q;
    cin >> q;

    for (int i = 0; i < q; i++) {
        int pocz, kon;
        cin >> pocz >> kon;
        int ile5, ile2;
        ile5 = licz5i2[kon].first - licz5i2[pocz - 1].first;
        ile2 = licz5i2[kon].second - licz5i2[pocz - 1].second;
        cout << min(ile5, ile2) << endl;
    }

    return 0;
}
