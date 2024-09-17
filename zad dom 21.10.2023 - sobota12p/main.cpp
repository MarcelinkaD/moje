// 2) Ryby (str. 33)
/*
#include <iostream>
#include <stack>
#include <vector>
using namespace std;

int main()
{
    stack<int> wsch;
    int n;
    cin >> n;
    int top;
    int l[n];
    int kol[n];
    int w;

    for (int i = 0; i < n; i++) {
        cin >> l[i];
    }

    for (int i = 0; i < n; i++) {
        cin >> kol[i];
    }

    for (int i = n - 1; i >= 0; i--) {
        if (kol[i] == 0) {
            wsch.push(l[i]);
        } else {
            while (!wsch.empty()) {
                top = wsch.top();
                if (top < l[i]) {
                    wsch.pop();
                } else {
                    break;
                }
            }
            if (wsch.empty()) {
                w++;
            }
        }
    }

    w += wsch.size();
    cout << w << endl;
    return 0;
}
*/

// 3) Cukierni [AKA Apteka] (str. 34)
#include <iostream>
using namespace std;

const int MAXN = 1000006;
const int INF = 1000000001;

bool czy_zmian[MAXN];
int n, t[MAXN], akt_min = INF, ost_zmian = -1;
long long wyn = 0;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> n;

    for (int i = 0; i < n; i++){
        cin >> t[i];
    }

    for (int i = n - 1; i >= 0; i--) {
        if (t[i] < akt_min) {
            czy_zmian[i] = 1;
            akt_min = t[i];
        }
    }

    for (int i = 0; i < n; i++) {
        if (czy_zmian[i]) {
            wyn += (long long) (i - ost_zmian) * t[i];
            ost_zmian = i;
        }
    }

    cout << wyn << endl;
}
