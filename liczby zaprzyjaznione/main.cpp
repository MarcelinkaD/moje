//https://szkopul.edu.pl/c/map-2024_2025/p/lpr/
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

ll s(int x){
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
    ll s1, s2;
    int a, b;
    cin >> a >> b;
    int wyn = 0;

    for (int akt_licz = a; akt_licz <= b; akt_licz++){
        s1 = s(akt_licz);
        if (s1 <= b && s1 >= a){
            s2 = s(s1);
            if (s2 == akt_licz && akt_licz < s1){
                cout << akt_licz << ' ' << s1 << endl;
                wyn++;
            }
        }
    }

    if (wyn == 0){
        cout << "BRAK" << endl;
    }
    return 0;
}
