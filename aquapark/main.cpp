#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, q;
    cin >> n >> q;
    vector<vector<int>> plansza(n + 1, vector<int>(n + 1));
    vector<vector<int>> pref(3 * n + 1, vector<int>(3 * n + 1));

    for (int i = 1; i <= n; i++){
        for (int j = 1; j <= n; j++){
            cin >> plansza[i][j];
        }
    }

    for (int i = 1; i <= n; i++){
        for (int j = 1; j <= n; j++){
            int ni = i + n;
            int nj = j + n;
            pref[ni][nj] = pref[ni - 1][nj] + plansza[i][j];
        }
    }

    while (q--){
        int i, j, l;
        cin >> i >> j >> l;
        i += n;
        j += n;
        int pole = 0;
        int ni = i;
        int ki = i;
        for (int nj = j - l; nj <= j + l; nj++){
            if (ni > n * 2){
                pole += pref[n * 2][nj];
            } else {
                pole += pref[ni][nj];
            }
            if (ki < n){
                pole -= pref[n][nj];
            } else {
                pole -= pref[ki - 1][nj];
            }
            if (nj < j){
                ni++;
                ki--;
            } else {
                ni--;
                ki++;
            }
        }
        cout << pole << '\n';
    }

    return 0;
}
