//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/czy/
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 10005;
bool dp[MAXN] = {false};

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    dp[0] = true;
    int n;
    cin >> n;

    for (int i = 0; i < n; i++){
        int w, l;
        cin >> w >> l;
        for (int j = MAXN - 1; j >= 0; j--){
            if (dp[j]){
                for (int k = 1; k <= l; k++){
                    if (j + k * w >= MAXN){
                        break;
                    }
                    dp[j + k * w] = true;
                }
            }
        }
    }

    int q;
    cin >> q;

    for (int i = 0; i < q; i++){
        int x;
        cin >> x;
        if (dp[x]){
            cout << "TAK" << endl;
        } else {
            cout << "NIE" << endl;
        }
    }

    return 0;
}
