//https://szkopul.edu.pl/c/map-2024_2025/p/dos/
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

ll dziel(int x){
    ll w = 1;
    int pierw = sqrt(x);

    for (int i = 2; i <= pierw; i++){
        if (x % i == 0){
            w += i;
            w += x / i;
        }
    }
    return w;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int q;
    cin >> q;

    while (q){
        int x;
        cin >> x;
        ll suma = dziel(x);
        if (suma == x){
            cout << "OK" << endl;
        } else if (suma < x){
            cout << "NIEDOSTATECZNA" << endl;
        } else {
            cout << "WIELKA" << endl;
        }
        q--;
    }
    return 0;
}
