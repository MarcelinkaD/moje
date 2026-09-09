#include <bits/stdc++.h>
using namespace std;

int main()
{
    string s;
    string x;
    while (cin >> x) {
        s += x;
    }

    int akt_licz = 0;
    int akt_wyn = 0;
    bool akt_dzial = 0;
    for (int i = 0; i < s.size(); i++){
        if (s[i] != '+' && s[i] != '-') {
            akt_licz *= 10;
            akt_licz += s[i] - '0';
        } else if (s[i] == '+'){
            if (akt_dzial == 0){
                akt_wyn += akt_licz;
            } else {
                akt_wyn -= akt_licz;
            }
            akt_dzial= 0;
            akt_licz = 0;
        } else {
            if (akt_dzial == 0){
                akt_wyn += akt_licz;
            } else {
                akt_wyn -= akt_licz;
            }
            akt_dzial= 1;
            akt_licz = 0;
        }
    }

    if (akt_dzial == 0){
        akt_wyn += akt_licz;
    } else {
        akt_wyn -= akt_licz;
    }

    cout << akt_wyn << endl;

    return 0;
}
