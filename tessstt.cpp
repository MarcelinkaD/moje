#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, q;
    cin >> n >> q;
    vector<vector<int>> graf(n + 1, vector<int>(n + 1));
    vector<vector<int>> pref(3 * n + 1, vector<int>(3 * n + 1));

    for (int i = 1; i <= n; i++){
        for (int j = 1; j <= n; j++){
            cin >> graf[i][j];
        }
    }

    for (int i = 1; i <= n; i++){
        for (int j = 1; j <= n; j++){
            int ni = i + n;
            int nj = j + n;
            pref[ni][nj] = pref[ni][nj - 1] + pref[ni - 1][nj] + graf[i][j] - pref[ni - 1][nj - 1];
        }
    }

    while (q--){
        int i, j, l;
        cin >> i >> j >> l;
        i += n;
        j += n;
        int pole = pref[i + l][j + l] - pref[i - l - 1][j + l] - pref[i + l][j - l - 1] + pref[i - l - 1][j - l  - 1];
        int nj = j + 1;
        for (int ni = i + l; ni > i; ni--){
            int do_odj = pref[i + l][nj] - pref[ni][nj - 1] - pref[ni - 1][nj] + pref[ni - 1][nj - 1];
            pole -= do_odj;
            nj++;
        }
        nj = j - l;
        for (int ni = i + 1; ni <= i + l; ni++){
            int do_odj = pref[i + l][nj] - pref[ni][nj - 1] - pref[ni - 1][nj] + pref[ni - 1][nj - 1];
            pole -= do_odj;
            nj++;
        }
        nj = j - l;
        for (int ni = i - 1; ni >= i - l; ni++){
            int do_odj = pref[ni][nj] - pref[i - l - 1][nj] - pref[i - l - 1][nj - 1] + pref[i - l - 1][nj - 1];
            pole -= do_odj;
            nj++;
        }
        cout << pole << '\n';
    }

    return 0;
}
