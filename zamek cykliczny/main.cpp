#include <iostream>
#include <string>
#include <queue>
#include <unordered_map>
#include <algorithm>
using namespace std;

unordered_map<string, int> odl;
queue<string> kol;

string na_odwrot (string n) {
    if (n.size() == 1) {
        return n;
    }

    string nowa_n = n.substr(1) + n[0];
    size_t ind = nowa_n.find_first_not_of('0');
    if (ind != string::npos)
        nowa_n = nowa_n.substr(ind);
    else
        nowa_n = "0";

    return nowa_n;
}

int bfs(string n) {
    odl[n] = 0;
    kol.push(n);

    while (!kol.empty()){
        string akt_licz = kol.front();
        kol.pop();

        string plus_jeden = akt_licz;
        int przeniesienie = 1;
        int akt_odl = odl[akt_licz];

        for (int i = plus_jeden.size() - 1; i >= 0 && przeniesienie; i--) {
            int cyfra = plus_jeden[i] - '0' + przeniesienie;
            przeniesienie = cyfra / 10;
            plus_jeden[i] = (cyfra % 10) + '0';
        }

        if (przeniesienie) {
            plus_jeden = '1' + plus_jeden;
        }

        if (odl.find(plus_jeden) == odl.end() || odl[plus_jeden] > akt_odl + 1) {
            odl[plus_jeden] = akt_odl + 1;

            if (plus_jeden == "1") {
                return odl[plus_jeden];
            }

            kol.push(plus_jeden);
        }

        string licz_na_odw = na_odwrot(akt_licz);

        if (odl.find(licz_na_odw) == odl.end() || odl[licz_na_odw] > akt_odl + 1) {
            odl[licz_na_odw] = akt_odl + 1;

            if (licz_na_odw == "1") {
                return odl[licz_na_odw];
            }

            kol.push(licz_na_odw);
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    string pocz_licz;
    cin >> pocz_licz;

    if (pocz_licz == "1"){
        cout << 0 << endl;
        return 0;
    }

    int ile_jed = 0;
    bool czy_zera_jed = 1;

    for (int i = 0; i < pocz_licz.size(); i++){
        if (pocz_licz[i] != '1' && pocz_licz[i] != '0'){
            czy_zera_jed = 0;
            break;
        }
        if (pocz_licz[i] == '1') {
            ile_jed++;
        }
    }

    if (czy_zera_jed) {
        if (ile_jed == 1) {
            cout << 1 << endl;
            return 0;
        }
        if (pocz_licz[pocz_licz.size() - 1] == '0') {
            cout << (19 + (ile_jed - 2) * 9) + 1 << endl;
        } else {
            cout << 19 + (ile_jed - 2) * 9 << endl;
        }
        return 0;
    }

    cout << bfs(pocz_licz) << endl;

    return 0;
}
