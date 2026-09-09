//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/inw/
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

vector<int> l;
const int MAXN = 3e5 + 5;
int drzewo[4 * MAXN];

void zmiana(int ind, int lewo, int prawo, int akt_wie) {
    if (lewo == prawo) {
        drzewo[ind]++;
        return;
    }
    int srodek = (lewo + prawo) / 2;
    if (akt_wie <= srodek)
        zmiana(2 * ind, lewo, srodek, akt_wie);
    else
        zmiana(2 * ind + 1, srodek + 1, prawo, akt_wie);
    drzewo[ind] = drzewo[2 * ind] + drzewo[2 * ind + 1];
}

int inwersje(int ind, int lewo, int prawo, int odp_lewo, int odp_prawo) {
    if (odp_prawo < lewo || odp_lewo > prawo)
        return 0;
    if (odp_lewo <= lewo && prawo <= odp_prawo)
        return drzewo[ind];
    int srodek = (lewo + prawo) / 2;
    return inwersje(2 * ind, lewo, srodek, odp_lewo, odp_prawo) +
           inwersje(2 * ind + 1, srodek + 1, prawo, odp_lewo, odp_prawo);
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;

    for (int i = 0; i < n; i++){
        int x;
        cin >> x;
        l.push_back(x);
    }

    vector<int> sorted = l;
    sort(sorted.begin(), sorted.end());
    for (int &x : l) {
        x = lower_bound(sorted.begin(), sorted.end(), x) - sorted.begin() + 1;
    }

    for (auto i : sorted){
        cout << i << ' ';
    }
    cout << endl;

    long long wyn = 0;
    for (int i = n - 1; i >= 0; --i) {
        wyn += inwersje(1, 1, n, 1, l[i] - 1);
        zmiana(1, 1, n, l[i]);
    }
    cout << wyn << endl;

    return 0;
}
