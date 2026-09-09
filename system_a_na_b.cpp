#include <bits/stdc++.h>
using namespace std;

string zmien(string x, int a, int b){
    int na_dzies = 0;
    int akt_pot = 1;
    for (int i = x.size() - 1; i >= 0; i--){
        if (x[i] >= (int)"A" && x[i] <= (int)"Z"){
            na_dzies += (int)(x[i] - 55) * akt_pot;
        } else {
            na_dzies += (int)(x[i]) * akt_pot;
        }
        akt_pot *= a;
    }

    if (na_dzies == 0) {
        return "0";
    }

    string wyn;
    while (na_dzies > 0){
        int reszta = na_dzies % b;
        if (reszta < 10){
            wyn += (char)(reszta + '0');
        } else {
            wyn += (char)(reszta + 'A' - 10);
        }
    }
    reverse(wyn.begin(), wyn.end());
    return wyn;
}

int main(){
    string x;
    
    return 0;
}