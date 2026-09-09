//gra w kamienie z potegami dwojki
/*#include <iostream>
typedef long long ll;
using namespace std;

int main()
{
    ll n;
    cin >> n;

    int reszta = n % 3;
    if (reszta == 0){
        cout << "Wygrywa gracz numer 2" << endl;
    } else {
        cout << "Wygrywa gracz numer 1" << endl;
    }

    return 0;
}
*/

//https://szkopul.edu.pl/problemset/problem/AWhdD7i4V7mupdKWVtpgfGSM/site/?key=statement
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

const int MAXN = 2e6 + 5;
pair<int, int> WYN[MAXN];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    for (int i = 0; i < MAXN; i++){
        WYN[i].first = -1;
        WYN[i].second = -1;
    }

    int n, q;
    string lizak;
    cin >> n >> q;
    cin >> lizak;

    int calk_sum = 0;
    int pierw_w = -1, ost_w;

    for (int i = 0; i < n; i++){
        if (lizak[i] == 'T'){
            calk_sum += 2;
        } else {
            calk_sum++;
            ost_w = i;

            if (pierw_w == -1){
                pierw_w = i;
            }
        }
    }

    int pocz = 0, kon = n - 1;
    int akt_sum = calk_sum;

    while (akt_sum > 0){
        WYN[akt_sum].first = pocz + 1;
        WYN[akt_sum].second = kon + 1;

        if (lizak[pocz] == 'T'){
            pocz++;
        } else if (lizak[kon] == 'T'){
            kon--;
        } else {
            pocz++;
            kon--;
        }
        akt_sum -= 2;
    }

    if (pierw_w <= n - 1 - ost_w) {
        pocz = pierw_w + 1;
        kon = n - 1;
        akt_sum = calk_sum - (2 * pierw_w) - 1;
    } else {
        pocz = 0;
        kon = ost_w - 1;
        akt_sum = calk_sum - 2 * ((n - 1) - ost_w) - 1;
    }

    while (akt_sum > 0){
        WYN[akt_sum].first = pocz + 1;
        WYN[akt_sum].second = kon + 1;

        if (lizak[pocz] == 'T'){
            pocz++;
        } else if (lizak[kon] == 'T'){
            kon--;
        } else {
            pocz++;
            kon--;
        }
        akt_sum -= 2;
    }

    while (q--){
        int k;
        cin >> k;

        if (WYN[k].first != -1) {
            cout << WYN[k].first << ' ' << WYN[k].second << endl;
        } else {
            cout << "NIE" << endl;
        }

    }

}
