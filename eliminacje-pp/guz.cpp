#include <bits/stdc++.h>
typedef long long ll;
#define int long long
using namespace std;

signed main(){
    int n, g;
    cin >> n >> g;

    if (g == 1){
        cout << -1 << endl;
        return 0;
    }
    if (g == n){
        cout << 4 << endl;
        return 0;
    }
    if (g % 2 == 0){
        cout << 0 << endl;
        return 0;
    }

    int y = (n / 2);
    int x = (g - 1) / 2;
    int wynik = 0;
    int j = n / (g - 1);
    for (int i = 1; i <= y; i++){
        
        if (__gcd(i, j) != 1){
            continue;
        }
        int kroki =  y / j;
        if (kroki == x){
            wynik += 4;
        }
    }

    if (wynik > 1000000000000000LL) {
        cout << -1 << endl;
        return 0;
    }
    cout << wynik << endl;
    
    return 0;
}