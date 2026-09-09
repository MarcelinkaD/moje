//AleMozgi 2024/2025
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1e6 + 7;
bool czy_wyst[MAXN];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    for (int i = 0 ; i < n; i++){
        int x;
        cin >> x;
        czy_wyst[x] = 1;
    }

    int max_wyn = 0;
    int akt_dl = 0;
    for (int i = 1; i < MAXN; i++){
        if (czy_wyst[i]){
            akt_dl++;
        } else {
            max_wyn += (akt_dl + 1) / 2;
            akt_dl = 0;
        }
    }
    max_wyn += (akt_dl + 1) / 2;
    cout << max_wyn << endl;

    return 0;
}
