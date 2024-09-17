/*
#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int tab[n + 1];

    for (int i = 1; i <= n; i++){
        cin >> tab[i];
    }

    int ile_zamian = 0;
    for (int i = 1; i <= n; i++) {
        if (i != tab[i]) {
            int index = tab[i];
            tab[i] = tab[index];
            tab[index] = index;
            ile_zamian++;
        }
    }

    if (ile_zamian <= 1) {
        cout << "TAK" << endl;
    } else {
        cout << "NIE" << endl;
    }

    return 0;
}
*/

#include <iostream>
using namespace std;

const int MAXN = 4;
bool l[MAXN];
int lewe[MAXN];
int prawe[MAXN];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;

    for (int i = 1; i <= n; i++){
        cin >> l[i];
    }

    for (int i = 1; i <= n; i++) {
        if (l[i] == 0) {
            lewe[i] = lewe[i - 1] + 1;
        } else {
            lewe[i] = lewe[i - 1];
        }
    }

    for (int i = n; i > 0; i--) {
        if (l[i] == 1) {
            prawe[i] = prawe[i + 1] + 1;
        } else {
            prawe[i] = prawe[i + 1];
        }
    }

    int w = prawe[1];
    for (int i = 1; i <= n; i++) {
        w = min(w, lewe[i] + prawe[i + 1]);
    }

    cout << w << endl;

    return 0;
}

