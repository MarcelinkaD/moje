#include <iostream>
#include <set>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    vector<vector<int>> graf;
    vector<vector<int>> graf2;
    set<int> sett;
    int n, k;
    cin >> n >> k;

    graf.resize(n + 1);
    graf2.resize(n + 1);
    for (int i = 0; i < k; i++) {
        int a, b;
        cin >> a >> b;
        graf[a].push_back(b);
        graf2[b].push_back(a);
    }

    for (int i = 1; i <= n; i++) {
        if (graf[i].size() == 0) {
            for (int k = 0; k < graf2[i].size(); k++) {
                sett.insert(graf2[i][k]);
            }
        }
    }

    cout << sett.size();
    return 0;
}
