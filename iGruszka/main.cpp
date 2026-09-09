//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/igr/
#include <bits/stdc++.h>
using namespace std;

vector<long long> l;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    long long ile_telefonow, koszt_za_jeden, n;
    cin >> ile_telefonow >> koszt_za_jeden >> n;

    int maxi = -1;
    for (int i = 0; i < n; i++){
        int x;
        cin >> x;
        maxi = max(maxi, x);
        l.push_back(x);
    }

    sort(l.begin(), l.end());

    long long max_wyn = 0;
    for (int i = 0; i < n; i++){
        long long akt_cena = l[i];
        long long zysk = (akt_cena - koszt_za_jeden) * min(n - i, ile_telefonow);
        max_wyn = max(max_wyn, zysk);
    }

    cout << max_wyn << endl;

    return 0;
}
