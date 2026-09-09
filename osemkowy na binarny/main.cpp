#include <bits/stdc++.h>
using namespace std;

int main()
{
    string n;
    cin >> n;

    int dzies = 0;
    int akt_pot = 1;
    for (int i = n.size() - 1; i >= 0; i--){
        char znak = n[i];
        int ile = (znak - '0') * akt_pot;
        akt_pot *= 8;
        dzies += ile;
    }

    vector<int> wyn;
    while (dzies){
        int reszta = dzies % 2;
        wyn.push_back(reszta);
        dzies /= 2;
    }

    reverse(wyn.begin(), wyn.end());
    for (auto i : wyn){
        cout << i;
    }

    return 0;
}
