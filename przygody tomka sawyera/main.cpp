#include <iostream>
#include <string>
using namespace std;

const int MAXN = 1e6 + 4;
int niebieskie[MAXN] = {0};

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int q;
    cin >> q;
    string plot;
    cin >> plot;
    int n = plot.size();

    for (int i = 1; i <= n; i++){
        if (plot[i - 1] == 'n') {
            niebieskie[i]++;
        }
        niebieskie[i] = niebieskie[i - 1] + niebieskie[i];
    }

    for (int k = 0; k < q; k++) {
        int pocz, kon;
        cin >> pocz >> kon;
        int licz_nieb = niebieskie[kon] - niebieskie[pocz - 1];
        int licz_ziel = (kon - pocz + 1) - licz_nieb;

        if (licz_nieb < licz_ziel) {
            cout << "z " << licz_ziel - licz_nieb << endl;
        } else if (licz_nieb > licz_ziel) {
            cout << "n " << licz_nieb - licz_ziel << endl;
        } else {
            cout << "labor omnia vincit" << endl;
        }
    }

    return 0;
}
