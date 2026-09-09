#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1e6 + 5;
vector<int> graf[MAXN];
pair<int, int> dp[MAXN];
int odp[MAXN];

void dfs1(int akt_wie, int rodzic){
    int naj_wyn = 0;
    int naj_wyn2 = 0;
    for (int sasiad : graf[akt_wie]){
        if (sasiad != rodzic){
            dfs1(sasiad, akt_wie);
            int akt_wyn = dp[sasiad].first + 1;
            if (akt_wyn > naj_wyn){
                swap(akt_wyn, naj_wyn);
            }
            if (akt_wyn > naj_wyn2){
                swap(akt_wyn, naj_wyn2);
            }
        }
    }
    dp[akt_wie] = {naj_wyn, naj_wyn2};
}

void dfs2(int akt_wie, int rodzic, int naj_rodzic){
    int naj_wyn = dp[akt_wie].first;
    int naj_wyn2 = dp[akt_wie].second;
    if (naj_rodzic > naj_wyn){
        swap(naj_rodzic, naj_wyn);
    }
    if (naj_rodzic > naj_wyn2){
        swap(naj_rodzic, naj_wyn2);
    }
    odp[akt_wie] = naj_wyn + naj_wyn2;
    for (int sasiad : graf[akt_wie]){
        if (sasiad != rodzic){
            int x = naj_wyn;
            if (x == dp[sasiad].first + 1){
                x = naj_wyn2;
            }
            dfs2(sasiad, akt_wie, x + 1);
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    for (int i = 0; i < n - 1; i++){
        int a, b;
        cin >> a >> b;
        graf[a].push_back(b);
        graf[b].push_back(a);
    }

    dfs1(1, 0);
    dfs2(1, 0, 0);

    for (int i = 1; i <= n; i++){
        cout << odp[i] << endl;
    }

    return 0;
}
