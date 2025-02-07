//https://szkopul.edu.pl/c/mistrz-programowania-2025/p/r1c/
#include <bits/stdc++.h>
using namespace std;

int na_co[10] = {0, 1, 2, 3, -1, 5, 9, -1, 8, 6};
vector<int> l;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;

    for (int i = 0; i < n; i++){
        char x;
        cin >> x;
        int licz = x - '0';
        l.push_back(licz);
    }

    for (int i = 0; i < n; i++){
        int akt_licz = l[i];
        int gdzie = n - i - 1;
        if (!(na_co[akt_licz] != -1 && akt_licz == na_co[l[gdzie]])) {
            cout << "NIE" << endl;
            return 0;
        }
    }

    cout << "TAK" << endl;
    return 0;
}
