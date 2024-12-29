//https://szkopul.edu.pl/c/map-2024_2025/p/zar/25364/
#include <iostream>
using namespace std;

const int MAXN = 1005;
int zar[MAXN];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n, m;
    cin >> n >> m;

    int w = 0;
    for (int i = 0; i < m; i++){
        int x;
        cin >> x;
        zar[x]++;
    }

    for (int i = 1; i <= n; i++){
        if (zar[i] % 2 == 1) {
            w++;
        }
    }

    cout << w << endl;

    return 0;
}
