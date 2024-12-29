//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/inn/
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1e6 + 5;
vector<int> graf[MAXN];
int ojciec[MAXN];
bool czy_odw[MAXN];

void wyznacz_ojca(int akt_wie) {
    czy_odw[akt_wie] = 1;
    for (int i = 0; i < graf[akt_wie].size(); i++){
        int sasiad = graf[akt_wie][i];
        if (!czy_odw[sasiad]){
            wyznacz_ojca(sasiad);
            ojciec[sasiad] = akt_wie;
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n, korzen;
    cin >> n >> korzen;

    for (int i = 0; i < n - 1; i++){
        int a, b;
        cin >> a >> b;
        graf[a].push_back(b);
        graf[b].push_back(a);
    }

    wyznacz_ojca(korzen);

    int q;
    cin >> q;

    for (int i = 0; i < q; i++){
        int x;
        cin >> x;
        if (x == korzen) {
            cout << "ADAM" << endl;
        } else {
            cout << ojciec[x] << endl;
        }
    }

    return 0;
}
