//https://szkopul.edu.pl/c/mistrz-programowania-2025/p/r3e/
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n, m;
    cin >> n >> m;
    int d = n;

    vector<vector<int>> ins;
    ins.reserve(m);

    for (int i = 0; i < m; i++){
        int u, v;
        cin >> u >> v;
        vector<int> instrukcja(d, 0);
        instrukcja[u - 1] = -1;
        instrukcja[v - 1] = 1;
        ins.push_back(instrukcja);
    }

    cout << d << endl;

    for (int i = 0; i < n; i++){
        vector<int> stan(d, 0);
        stan[i] = 1;
        for (int j = 0; j < d; j++){
            cout << stan[j] << ' ';
        }
        cout << endl;
    }

    cout << ins.size() << endl;
    for (auto &instrukcja : ins) {
        for (int i = 0; i < d; i++){
            cout << instrukcja[i] << ' ';
        }
        cout << endl;
    }

    return 0;
}
