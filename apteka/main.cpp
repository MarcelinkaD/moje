#include <iostream>
using namespace std;

typedef long long int ll;

const int MAXN = 1000006;
const int INF = 1000000001;

bool swapWith[MAXN];
int n, t[MAXN], curMin = INF, lastSwap = -1;
ll wyn = 0;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> n;

    for (int i = 0; i < n; i++){
        cin >> t[i];
    }

    for (int i = n - 1; i >= 0; i--) {
        if (t[i] < curMin) {
            curMin = t[i];
            swapWith[i] = 1;
        }
    }

    for (int i = 0; i < n; i++){
        if (swapWith[i]) {
            wyn += (ll) (i - lastSwap) * t[i];
            lastSwap = i;
        }
    }

	cout << wyn << endl;

    return 0;
}
