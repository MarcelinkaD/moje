// 1) https://szkopul.edu.pl/problemset/problem/6x4-Pmy-UoyrQpi19NsAz6Rn/site/?key=statement
/*#include <bits/stdc++.h>
using namespace std;

struct hashFunction{
    size_t operator()(const pair<long long, long long> &x) const
  {
    return x.first * (2*1e9) + x.second;
  }
};

const int p = 37;
const long long mod = 1000000033;
const long long MAXN = 2 * 1e5 + 5;
const long long pol_MAXN = 1e5 + 5;

long long pot[MAXN];
long long hasz_lewo[MAXN];
long long hasz_prawo[MAXN];
int n;
vector<int> l;
vector<int> naj_k;

long long haszowanie_lewo(int pocz, int kon) {
    return ((hasz_lewo[kon] - hasz_lewo[pocz - 1] + mod) * pot[n - kon] % mod);
}

long long haszowanie_prawo(int pocz, int kon) {
    return ((hasz_prawo[pocz] - hasz_prawo[kon + 1] + mod) * pot[pocz - 1] % mod);
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n;

    l.push_back(0);
    for (int i = 0; i < n; i++){
        int x;
        cin >> x;
        l.push_back(x);
    }

    pot[0] = 1;
    for (int i = 1; i <= n; i++) {
      pot[i] = pot[i - 1] * p % mod;
      hasz_lewo[i] = (hasz_lewo[i - 1] + l[i] * pot[i]) % mod;
    }

    for (int i = n; i >= 1; i--) {
      hasz_prawo[i] = (hasz_prawo[i + 1] + l[i] * pot[n - i + 1]) % mod;
    }

    int max_wyn = -1;
    for (int akt_dlu = 0; akt_dlu < n; akt_dlu++){
        unordered_set<pair<long long, long long>, hashFunction> pary;
        for (int i = 1; i <= n - akt_dlu; i += (akt_dlu + 1)){
            long long od_lewo = haszowanie_lewo(i, i + akt_dlu);
            long long od_prawo = haszowanie_prawo(i, i + akt_dlu);
            pary.insert({min(od_lewo, od_prawo), max(od_lewo, od_prawo)});
        }
        int ile = pary.size();
        if (max_wyn < ile){
            max_wyn = ile;
            naj_k.clear();
        }
        if (ile == max_wyn) {
            naj_k.push_back(akt_dlu + 1);
        }
    }

    cout << max_wyn << ' ' << naj_k.size() << endl;
    for (int i : naj_k) {
        cout << i << ' ';
    }

    return 0;
}*/

// 2) https://cses.fi/alon/task/1744
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 505;
int dp[MAXN][MAXN];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int a, b;
    cin >> a >> b;

    if (a == b) {
        cout << 0 << endl;
        return 0;
    }

    for (int i = 1; i <= a; i++){
        for (int j = 1; j <= b; j++){
            if (i == 1) {
                dp[i][j] = j - 1;
            } else if (j == 1) {
                dp[i][j] = i - 1;
            } else if (i == j) {
                dp[i][j] = 0;
            } else {
                int min_wyn1 = MAXN;
                for (int k = 1; k < i; k++){
                    min_wyn1 = min(min_wyn1, 1 + dp[k][j] + dp[i - k][j]);
                }
                int min_wyn2 = MAXN;
                for (int k = 1; k < j; k++){
                    min_wyn2 = min(min_wyn2, 1 + dp[i][k] + dp[i][j - k]);
                }
                dp[i][j] = min(min_wyn1, min_wyn2);
            }
        }
    }

    cout << dp[a][b] << endl;

    return 0;
}
