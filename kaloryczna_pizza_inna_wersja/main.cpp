//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/kal/
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

vector<ll> pref;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    ll suma = 0;
    pref.push_back(0);
    for (int i = 0; i < n; i++){
        int x;
        cin >> x;
        suma += x;
        pref.push_back(suma);
    }

    int q;
    cin >> q;
    for (int i = 0; i < q; i++){
        int pocz, kon;
        cin >> pocz >> kon;
        cout << pref[kon] - pref[pocz - 1] << endl;
    }
    return 0;
}
