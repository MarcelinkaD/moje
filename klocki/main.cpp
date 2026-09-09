#include <bits/stdc++.h>
using namespace std;

vector<int> klocki;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    for (int i = 0; i < n; i++){
        int x;
        cin >> x;
        klocki.push_back(x);
    }

    while(m--){
        int k;
        cin >> k;
        vector<int> roznice;
        for (int i = 0; i < n; i++){
            roznice.push_back(klocki[i] - k);
        }

        vector<int> pref;
        pref[0] = roznice[0];
        for (int i = 1; i < n; i++){
            pref[i] = pref[i - 1] + roznice[i];
        }

        set<pair<int, int>> mini_prefi;
        mini_prefi.insert({pref[0], 0});
        for (int i = 1; i < n; i++){
            if (*mini_prefi.begin().first >= pref[i]){
                mini_prefi.insert({pref[i], i});
            }
        }

        set<pair<int, int>> maxi_sufi;
        maxi_sufi.insert({pref[n - 1], n - 1});
        for (int i = n - 1; i >= 0; i--){
            if (*maxi_sufi.rbegin().first < pref[i]){
                maxi_sufi.insert({pref[i], i});
            }
        }
    }

    return 0;
}
