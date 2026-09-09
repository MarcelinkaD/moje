//https://szkopul.edu.pl/c/konkurs-przed-obozem-oki-2025/p/zol/
#include <bits/stdc++.h>
using namespace std;

vector<int> il;

bool czy_git(int x, int n){
    int i = 0;
    int jaki_rzad = 0;
    int akt_wolne = x;
    while (jaki_rzad < x){
        int reszta = akt_wolne - il[i];
        if (reszta < 0){
            akt_wolne = x;
            jaki_rzad++;
        } else {
            i++;
            if (i == n){
                return true;
            }
            akt_wolne = reszta;
        }
    }
    if (i == n){
        return true;
    } else {
        return false;
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    int mini = INT_MAX;
    int maxi = n;

    for (int i = 0; i < n; i++){
        int x;
        cin >> x;
        il.push_back(x);
        mini = min(mini, x);
        maxi = max(maxi, x);
    }

    if (maxi != n){
        mini = maxi;
    }

    while (mini < maxi){
        int srodek = (mini + maxi) / 2;
        if (czy_git(srodek, n)){
            maxi = srodek;
        } else {
            mini = srodek + 1;
        }
    }

    cout << mini << endl;

    return 0;
}
