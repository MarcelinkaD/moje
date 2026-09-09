//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/tro2/21796/
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 360005;
bool l[MAXN];
vector<vector<int>> wyn;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int p, q, n;
    cin >> p >> q >> n;

    if (p > q){
        int temp = p;
        p = q;
        q = temp;
    }

    int x, y, z;
    for (int i = 1; i <= n; i++){
        if (l[i] == false){
            x = i;
            y = i + p;
            z = i + p + q;

            if (l[y]){
                y = i + q;
            }

            l[x] = true;
            l[y] = true;
            l[z] = true;

            wyn.push_back({x, y, z});
        }
    }

    cout << wyn.size() << endl;
    for (int i = 0; i < wyn.size(); i++){
        cout << wyn[i][0] << ' ' << wyn[i][1] << ' ' << wyn[i][2] << endl;
    }

    return 0;
}
