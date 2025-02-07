//https://szkopul.edu.pl/c/mistrz-programowania-2025/p/r4c/
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1e9 + 7;
unordered_map<int, int> zak;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;
    int m = 0;
    for (int k = 0; k < n; k++) {
        int p;
        cin >> p;
        int akt_ind = 0;
        int suma = 0;
        for (int i = 0; i < p; i++) {
            int x;
            cin >> x;
            akt_ind += x;
            zak[akt_ind]++;
            suma += x;
        }
        m = suma;
    }

    int min_wyn = MAXN;
    int max_wyn = -1;
    auto kon = zak.end();

    for (const auto& para : zak){
        if (para.first != m) {
            min_wyn = min(min_wyn, n - para.second);
            max_wyn = max(max_wyn, n - para.second);
        }
    }

    if (zak.size() != m) {
        max_wyn = max(max_wyn, n);
    }

    min_wyn = min(min_wyn, max_wyn);

    cout << min_wyn << ' ' << max_wyn << endl;

    return 0;
}
