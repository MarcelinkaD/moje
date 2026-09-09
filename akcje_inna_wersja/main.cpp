//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/akc/
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    int akt_min = 1e9;
    int max_wyn = 0;
    for (int i = 0; i < n; i++){
        int x;
        cin >> x;
        max_wyn = max(max_wyn, x - akt_min);
        akt_min = min(akt_min, x);
    }
    cout << max_wyn << endl;

    return 0;
}
