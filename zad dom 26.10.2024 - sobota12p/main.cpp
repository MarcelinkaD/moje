// 1) https://cses.fi/problemset/task/1649
/*#include <iostream>
#include <vector>
#define ll long long
using namespace std;

const int R = (1 << 18);
ll drzewo[2 * R];

void zamien(int k, int u) {
    k += R;
    drzewo[k] = u;

    while(k > 1) {
        k /= 2;
        drzewo[k] = min(drzewo[2 * k], drzewo[2 * k + 1]);
    }
}

ll minimalny_na_przedziale(int pocz, int kon) {
    pocz += R;
    kon += R;

    if (pocz == kon) {
        return drzewo[pocz];
    }

    ll w = min(drzewo[pocz], drzewo[kon]);

    while (pocz != kon - 1) {
        if (pocz % 2 == 0) {
            w = min(w, drzewo[pocz + 1]);
        }
        if (kon % 2 == 1) {
            w = min(w, drzewo[kon - 1]);
        }

        pocz /= 2;
        kon /= 2;
    }
    return w;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n, q;
    cin >> n >> q;

    for (int i = 1; i <= n; i++) {
        cin >> drzewo[i + R];
    }

    for (int i = R - 1; i >= 1; i--) {
        drzewo[i] = min(drzewo[2 * i], drzewo[2 * i + 1]);
    }

    for (int i = 0; i < q; i++) {
        int rodzaj;
        cin >> rodzaj;
        if (rodzaj == 1) {
            int k, u;
            cin >> k >> u;
            zamien(k, u);
        } else {
            int pocz, kon;
            cin >> pocz >> kon;
            cout << minimalny_na_przedziale(pocz, kon) << endl;
        }
    }

    return 0;
}*/

// 2.1)  https://szkopul.edu.pl/problemset/problem/LLIZxKm7TnxiId6MwlB479un/site/?key=statement (merge sort)
/*#include <iostream>
#include <vector>
#define ll long long
using namespace std;

const int MAXN = 300000;
int l[MAXN];
ll wyn = 0;

void polacz(int pocz, int srodek, int kon) {
    int lewo = pocz;
    int prawo = srodek + 1;
    int akt = 0;
    vector<int> temp(kon - pocz + 1);

    while (lewo <= srodek && prawo <= kon){
        if (l[lewo] <= l[prawo]) {
            temp[akt] = l[lewo];
            lewo++;
        } else {
            temp[akt] = l[prawo];
            prawo++;
            wyn += srodek - lewo + 1;
        }
        akt++;
    }

    while (lewo <= srodek){
        temp[akt] = l[lewo];
        lewo++;
        akt++;
    }

    while (prawo <= kon){
        temp[akt] = l[prawo];
        prawo++;
        akt++;
    }

    for (int i = 0; i < temp.size(); i++){
        l[pocz + i] = temp[i];
    }
}


void merge_sort(int pocz, int kon){
    if (pocz == kon){
        return;
    }
    int srodek = (pocz + kon) / 2;

    merge_sort(pocz, srodek);
    merge_sort(srodek + 1, kon);
    polacz(pocz, srodek, kon);

}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;

    for (int i = 0; i < n; i++){
        cin >> l[i];
    }

    merge_sort(0, n - 1);

    for (int i = 0; i < n; i++){
        cout << l[i] << ' ';
    }

    cout << endl;
    cout << wyn;

    return 0;
}*/

// 2.2) https://szkopul.edu.pl/problemset/problem/LLIZxKm7TnxiId6MwlB479un/site/?key=statement (inwersje rekurencyjnie)
#include <iostream>
#include <vector>
#include <algorithm>
#define ll long long
using namespace std;

vector<int> l;
ll wyn = 0;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;

    for (int i = 0; i < n; i++){
        int x;
        cin >> x;
        l.push_back(x);
    }

    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (l[i] > l[j])
                wyn++;
        }
    }

    sort(l.begin(), l.end());

    for (int i = 0; i < n; i++){
        cout << l[i] << ' ';
    }

    cout << endl;
    cout << wyn;

    return 0;
}
