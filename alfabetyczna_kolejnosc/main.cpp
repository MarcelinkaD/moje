//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/alf/
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

const int MAXN = 1000005;
vector<int> graf[MAXN];
int wchadzace[MAXN];
priority_queue<int> kol;
vector<int> wyn;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n, m, ile_odw = 0;
    cin >> n >> m;

    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        graf[a].push_back(b);
        wchadzace[b]++;
    }

    for (int i = 1; i <= n; i++) {
        if (wchadzace[i] == 0) {
            kol.push(-i);
        }
    }

    while (!kol.empty()) {
        int u = kol.top();
        u *= -1;
        kol.pop();

        ile_odw++;
        wyn.push_back(u);

        for (int i = 0; i < graf[u].size(); i++) {
            int sasiad = graf[u][i];
            wchadzace[sasiad] -= 1;
            if (wchadzace[sasiad] == 0) {
                kol.push(-sasiad);
            }
        }
    }

    if (ile_odw != n) {
        cout << "UNMOGLICH" << endl;
    } else {
        for (int i = 0; i < n; i++) {
            cout << wyn[i] << ' ';
        }
    }

    return 0;
}
