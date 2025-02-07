//https://szkopul.edu.pl/c/mistrz-programowania-2025/p/r0b/
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;

    if (n != 13) {
        cout << "OSZUST!" << endl;
        return 0;
    }

    int w = 0;
    unordered_set<string> legitne_karty = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"};
    unordered_map<string, int> ilosc;

    for (int i = 0; i < n; i++){
        string x;
        cin >> x;

        auto czy_jest = legitne_karty.find(x);
        if (czy_jest == legitne_karty.end()) {
            cout << "OSZUST!" << endl;
            return 0;
        }

        ilosc[x]++;
        if (ilosc[x] > 4) {
            cout << "OSZUST!" << endl;
            return 0;
        }

        if (x == "J") w++;
        if (x == "Q") w += 2;
        if (x == "K") w += 3;
        if (x == "A") w += 4;
    }

    cout << w << endl;
    return 0;
}
