// https://szkopul.edu.pl/c/map-2024_2025/p/ban/
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;

    int kto[n + 1];
    bool czy_odw[n + 1];

    for (int i = 1; i <= n; i++){
        int x;
        cin >> x;
        kto[i] = x;
        czy_odw[i] = 0;
    }

    int w = 0;
    for (int i = 1; i < n + 1; i++) {
        int akt_ind = i;
        if (!czy_odw[akt_ind]) {
            w++;
            while (!czy_odw[akt_ind]) {
                czy_odw[akt_ind] = 1;
                akt_ind = kto[akt_ind];
            }
        }
    }

    cout << w << endl;
    return 0;
}
