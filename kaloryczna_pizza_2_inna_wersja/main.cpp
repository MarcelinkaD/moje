//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/kap/
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

const int MAXN = 1005;
long long pref[MAXN][MAXN];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    cin >> n >> m;
    for (int i = 1; i <= n; i++){
        for (int j = 1; j <= m; j++){
            cin >> pref[i][j];
        }
    }

    for (int i = 1; i <= n; i++){
        for (int j = 1; j <= m; j++){
            pref[i][j] = pref[i][j - 1] + pref[i - 1][j] + pref[i][j] - pref[i - 1][j - 1];
        }
    }

    int q;
    cin >> q;
    for (int k = 0; k < q; k++){
        int i1, j1, i2, j2;
        cin >> i1 >> j1 >> i2 >> j2;
        cout << pref[i2][j2] - pref[i2][j1 - 1] - pref[i1 - 1][j2] + pref[i1 - 1][j1 - 1] << endl;
    }

    return 0;
}
