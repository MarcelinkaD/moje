//https://szkopul.edu.pl/c/map-2024_2025/p/sbp/
#include <bits/stdc++.h>
using namespace std;

bool czy_pierw(int x){
    int pierw = sqrt(x);
    if (x == 0 || x == 1) return 0;
    for (int i = 2; i <= pierw; i++){
        if (x % i == 0){
            return 0;
        }
    }
    return 1;
}

int suma(int x, int pod){
    int wyn = 0;
    while (x > 0){
        wyn += x % pod;
        x /= pod;
    }
    return wyn;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int pocz, kon;
    cin >> pocz >> kon;

    int w = 0;
    for (int akt_licz = pocz; akt_licz <= kon; akt_licz++){
        if (czy_pierw(akt_licz)){
            int s1 = suma(akt_licz, 10);
            int s2 = suma(akt_licz, 2);
            if (czy_pierw(s1) && czy_pierw(s2)){
                w += 1;
            }
        }
    }
    cout << w << endl;
    return 0;
}
