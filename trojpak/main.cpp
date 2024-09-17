#include <iostream>
#include <vector>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;
    vector<int> l;
    int ile_czego[4] = {0, 0, 0, 0};
    int ile_mamy[4] = {0, 0, 0, 0};

    for (int i = 0; i < n; i++){
        int x;
        cin >> x;
        l.push_back(x);
    }

    for (int k = 1; k <= 3; k++) {
        int q;
        cin >> q;
        ile_czego[k] = q;
    }

    int pocz, kon, wynik, akt_dlu, dlu_troj;
    pocz = -1;
    kon = 0;
    wynik = 0;
    akt_dlu = 0;
    dlu_troj = ile_czego[1] + ile_czego[2] + ile_czego[3];

    while (kon < n) {
        while (pocz < n - 1 && akt_dlu < dlu_troj) {
            pocz++;
            ile_mamy[l[pocz]]++;
            akt_dlu++;

            if (ile_mamy[1] == ile_czego[1] && ile_mamy[2] == ile_czego[2] && ile_mamy[3] == ile_czego[3]) {
                wynik++;
            }
        }

        ile_mamy[l[kon]]--;
        kon++;
        akt_dlu--;

        if (ile_mamy[1] == ile_czego[1] && ile_mamy[2] == ile_czego[2] && ile_mamy[3] == ile_czego[3]) {
            wynik++;
        }
    }

    cout << wynik << endl;

    return 0;
}
