//https://szkopul.edu.pl/c/map-2024_2025/p/sys/
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

vector<char> w;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    unordered_map<char, int> klucz;

    for (char lit = 'A'; lit <= 'Z'; ++lit) {
        klucz[lit] = 10 + (lit - 'A');
    }

    string x;
    int y, z;
    cin >> x >> y >> z;

    ll na_10 = 0;
    ll akt_pot = 1;
    for (int i = x.size() - 1; i >= 0; i--){
        char znak = x[i];
        int licz = (int)znak - 48;
        if (licz > 9) {
            licz = klucz[znak];
        }
        na_10 += akt_pot * licz;
        akt_pot *= y;
    }

    int mod;

    while (na_10 != 0){
        mod = na_10 % z;
        if (mod > 9){
            mod -= 10;
            w.push_back(char(mod + 65));
        } else {
            w.push_back(char(mod + 48));
        }
        na_10 /= z;
    }

    for (int i = w.size() - 1; i >= 0; i--) {
        cout << w[i];
    }

    return 0;
}
