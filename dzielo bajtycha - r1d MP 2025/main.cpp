//https://szkopul.edu.pl/c/mistrz-programowania-2025/p/r1d/
#include <bits/stdc++.h>
#define ll long long
using namespace std;

const int INF = 1e7 + 5;
const int MAXN = 1e5 + 5;
static int dp[MAXN][505][2];

int n, k;
int l[MAXN];
vector<int> graf[MAXN];
int temp[501][2];

void dfs(int v) {
    for (int j = 0; j <= k; j++) {
        dp[v][j][0] = -INF;
        dp[v][j][1] = -INF;
    }
    dp[v][0][0] = 0;
    if (k >= 1) {
        dp[v][1][1] = l[v];
    }

    for (int sasiad : graf[v]) {
        dfs(sasiad);

        for (int j = 0; j <= k; j++) {
            temp[j][0] = -INF;
            temp[j][1] = -INF;
        }

        for (int j = 0; j <= k; j++) {
            if (dp[v][j][0] == -INF) {
                continue;
            }

            for (int x = 0; x <= k - j; x++) {
                int naj_w = max(dp[sasiad][x][0], dp[sasiad][x][1]);
                if (naj_w == -INF){
                    continue;
                }

                temp[j + x][0] = max(temp[j + x][0], dp[v][j][0] + naj_w);
            }
        }


        for (int j = 0; j <= k; j++) {
            temp[j][1] = max(temp[j][1], dp[v][j][1]);
        }

        for (int j = 0; j <= k; j++) {
            dp[v][j][0] = temp[j][0];
            dp[v][j][1] = temp[j][1];
        }
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n >> k;
    for (int i = 1; i <= n; i++) {
        cin >> l[i];
    }
    for (int i = 2; i <= n; i++) {
        int a;
        cin >> a;
        graf[a].push_back(i);
    }

    dfs(1);

    int wynik = max(dp[1][k][0], dp[1][k][1]);
    if (wynik < 0) {
        wynik = -1;
    }
    cout << wynik << endl;

    return 0;
}
