#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1e6 + 5;
bool czy_jest[MAXN];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    for (int i = 0; i < n; i++){
        int x;
        cin >> x;
        czy_jest[x] = 1;
    }

    for (int i = 0; i < MAXN; i++){
        if (czy_jest[i] == 0){
            cout << i << endl;
            return 0;
        }
    }

    return 0;
}
