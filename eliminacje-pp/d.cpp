#include <bits/stdc++.h>

using namespace std;

int main() {
    int t; cin >> t;
    while (t--) {
        int w, k; cin >> w >> k;
        if (k > w) {
            swap(w, k);
        }
        cout << w * ( k / 2) +( k % 2 == 0 ? 0 :  w / 2 )<< "\n";
    }
}