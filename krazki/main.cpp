//https://szkopul.edu.pl/c/map-2024_2025/p/kra/22045/
#include <bits/stdc++.h>
using namespace std;

vector<int> l;
int INF = 1e9 + 7;

int znajdz(int k, int pocz, int kon){
    int srodek;
    while (pocz < kon) {
        srodek = (pocz + kon) / 2;
        if (l[srodek] < k) {
            kon = srodek;
        } else {
            pocz = srodek + 1;
        }
    }
    return pocz;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n, m;
    cin >> n >> m;
    int pop = INF;
    l.push_back(INF);

    for (int i = 0; i < n; i++){
        int x;
        cin >> x;
        if (x > pop) {
            l.push_back(pop);
        } else {
            l.push_back(x);
            pop = x;
        }
    }
    int pocz = 0;
    int kon = n + 1;
    int w;

    for (int i = 0; i < m; i++){
        int krazek;
        cin >> krazek;
        int ind = znajdz(krazek, pocz, kon);

        if (ind == 0) {
            cout << 0 << endl;
            return 0;
        }

        kon = ind - 1;
    }

    cout << kon << endl;

    return 0;
}
