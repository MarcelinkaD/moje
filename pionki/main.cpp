//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/pio/
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1e6 + 5;
int kolumny[MAXN];

int main()
{
    int n, m;
    cin >> n >> m;

    int max_wie = -1, max_kol = -1;
    int suma = 0;
    for (int i = 0; i < n; i++){
        int akt_wie = 0;
        for (int j = 0; j < m; j++){
            char x;
            cin >> x;
            if (x == '#'){
                akt_wie++;
                kolumny[j]++;
                suma++;
            }
        }
        max_wie = max(max_wie, akt_wie);
    }

    for (int j = 0; j < m; j++){
        max_kol = max(max_kol, kolumny[j]);
    }

    int wyn = max_wie + max_kol + 2 * (suma - (max_wie + max_kol));
    cout << wyn << endl;

    return 0;
}
