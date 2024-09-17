#include <iostream>
using namespace std;

int miasta_po_kolei[1000100], co_dla_kogo[1000100];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int n;
    cin >> n;
    int wyn = 1;

    for (int i = n; i > 0; i--) {
        int w;
        cin >> w;
        miasta_po_kolei[i] = w;
    }

    for (int i = 1; i <= n; i++) {
        int m;
        cin >> m;
        co_dla_kogo[m] = i;
    }

    for (int i = 1; i <= n; i++) {
        miasta_po_kolei[i] = co_dla_kogo[miasta_po_kolei[i]];
    }

    for (int i = 1; i < n; i++) {
        if ((miasta_po_kolei[i + 1] < miasta_po_kolei[i] && miasta_po_kolei[i + 1] > 1) || (i > 1 && miasta_po_kolei[i] == 1)) {
            wyn++;
        }
    }

    cout << wyn << endl;

    return 0;
}
