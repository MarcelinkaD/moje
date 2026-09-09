//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/kon/54930/
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

//const int MAXN = 605;
//const int MAXK = 55;
const int MAXN = 7;
const int MAXK = 3;
ll dp[MAXN][MAXK];
ll l[MAXN][MAXN];
ll pref[MAXN][MAXN];

ll suma(int akt_stacja, int n){
    int ile_w_rzedzie = n - akt_stacja;
    int akt_ind = n - 1 - ile_w_rzedzie;

    if (akt_stacja == 1){
        return pref[akt_stacja][n - 1];
    }

    ll s1 = pref[akt_stacja][n - 1];
    ll s2 = pref[akt_stacja][akt_ind];
    return s1 - s2;
}

ll suma_prost(int x1, int y1, int x2, int y2){
    ll s1 = pref[x2][y2];
    ll s2 = pref[x1 - 1][y2];
    ll s3 = pref[x2][y1 - 1];
    ll s4 = pref[x1 - 1][y1 - 1];
    s1 -= s2;
    s1 -= s3;
    s1 += s4;
    return s1;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, k;
    cin >> n >> k;

    for (int i = 1; i <= n; i++){
        int akt_ind;
        for (int j = 0; j < n - i; j++){
            akt_ind = j + i;
            cin >> l[i][akt_ind];
        }
    }

    for (int i = 1; i < MAXN; i++){
        for (int j = 1; j < MAXN; j++){
            pref[i][j] = pref[i - 1][j] + pref[i][j - 1] + l[i][j] - pref[i - 1][j - 1];
        }
    }

    dp[0][0] = 0;
    for (int i = 1; i < MAXN; i++){
        dp[i][0] = 0;
        dp[i][1] = suma(i, n);
        ll max_wyn = -1;
        for (int j = 2; j < MAXK; j++){
            for (int k = i; k > 0; k--){
                k--;
                int ile_w_rzedzie = n - i;
                int akt_ind = n - ile_w_rzedzie;
                max_wyn = max(max_wyn, dp[k][j - 1] + suma_prost(i - k + 1, akt_ind, i, n - 1));
            }
            dp[i][j] = max_wyn;
        }
    }

    /*for (int i = 0; i < MAXN; i++){
        for (int j = 0; j < MAXK; j++){
            cout << dp[i][j] << ' ';
        }
        cout << endl;
    }*/

    return 0;
}
