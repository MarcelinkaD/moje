//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/eas/
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1e6 + 5;
const int INF = 1e7 + 5;
vector<int> graf[MAXN];
bool czy_odw[MAXN];
int dp[MAXN][3];

void min_zbior_dom(int akt_wie) {
    czy_odw[akt_wie] = 1;
    dp[akt_wie][1] = 1;
    int min_roz = INF;
    for (int i = 0; i < graf[akt_wie].size(); i++) {
        int sasiad = graf[akt_wie][i];
        if (!czy_odw[sasiad]) {
            min_zbior_dom(sasiad);
            dp[akt_wie][1] += dp[sasiad][0];
            dp[akt_wie][2] += dp[sasiad][2];
            dp[akt_wie][0] += dp[sasiad][2];
            min_roz = min(min_roz, dp[sasiad][1] - dp[sasiad][2]);
        }
    }
    dp[akt_wie][2] += min_roz;
    dp[akt_wie][2] = min(dp[akt_wie][2], dp[akt_wie][1]);
    dp[akt_wie][0] = min(dp[akt_wie][2], dp[akt_wie][0]);
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;

    for (int i = 0; i < n - 1; i++){
        int a, b;
        cin >> a >> b;
        graf[a].push_back(b);
        graf[b].push_back(a);
    }

    min_zbior_dom(1);

    cout << dp[1][2] << endl;

    return 0;
}
