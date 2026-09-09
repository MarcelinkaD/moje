#include <bits/stdc++.h>
using namespace std;
int main() {
    int n, k; cin >> n >> k;
    string owce;
    cin >> owce;
    int l = 0;
    int r = 0;
    int liczba = 0;
    int suma = 0;
    while (r < n && owce[l] == 'C') {
        l ++;
        r ++;
    }
    while (r < n && liczba < k) {
        
        if (owce[r] == 'C') {
            suma ++;
        } else {
            liczba ++;
        }
        r++;
    }
    if (liczba != k) {
        cout << "NIE\n";
        return 0;
    }
    int najlepsza = suma;
    r--;
    while (r < n - 1 && l < r) {
        l ++;
        while (owce[l] == 'C' && l < r) {
            l ++;
            suma --;
        }
        r ++;
        while (owce[r] == 'C' && r < n) {
            r ++ ;
            suma ++;

        }
        najlepsza = min(najlepsza, suma);
    }
    cout << najlepsza << endl;
}