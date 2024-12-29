#include <iostream>
#include <string>
#include <queue>
#include <unordered_map>
#include <algorithm>
using namespace std;

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
    unordered_map<string, int> odl;
    queue<string> kol;
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

    for (int i = 1; i <= 100; i++){
        string pocz_licz = to_string(i);
        /*string pocz_licz = "";
        int k = i;
        string znak;
        while (k > 0){
            znak = to_string(k % 2);
            pocz_licz = znak + pocz_licz;
            k /= 2;
        }*/

        if (pocz_licz == "1"){
            cout << pocz_licz << " -> " << 0 << endl;
        } else {
            cout << pocz_licz << " -> " << bfs(pocz_licz) << endl;
        }


    }

    return 0;
}
