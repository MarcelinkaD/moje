#include <bits/stdc++.h>
using namespace std;

const int MAXN = 65005;
bool SIDO[MAXN];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    SIDO[0] = 1;
    SIDO[1] = 1;
    for (int i = 2; i < MAXN; i++){
        if (SIDO[i] == 0){
            for (int j = i + i; j < MAXN; j += i){
                SIDO[j] = 1;
            }
        }
    }

    int n;
    cin >> n;
    while (n != 1){
        if (SIDO[n] == 0){
            cout << "TAK" << '\n';
        } else {
            cout << "NIE" << '\n';
        }
        cin >> n;
    }

    return 0;
}
