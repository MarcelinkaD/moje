#include <bits/stdc++.h>
using namespace std;

string na_bin(int x, int n){
    string w;
    while (x != 0){
        char znak = ((x % 2) + '0');
        w = znak + w;
        x /= 2;
    }
    while (w.size() < n){
        w = '0' + w;
    }
    return w;
}

string zamiana(string x){
    string w;
    for (auto i : x){
        if (i == '0'){
            w += '1';
        } else {
            w += '0';
        }
    }
    return w;
}

string dodaj(string x, int n){
    string w;
    int prze = 1;
    for (int i = n - 1; i >= 0; i--){
        int akt_licz = x[i] - '0';
        char akt_znak;
        if (akt_licz + prze > 1){
            prze = 1;
            akt_znak = '0';
        } else {
            akt_znak = (akt_licz + prze) + '0';
            prze = 0;
        }
        w = akt_znak + w;
    }
    return w;
}

int main(){
    // zakladamy ze uzytkownik jest ogarniety i nie poda rzeczy poza limit
    int licz;
    int licz_bit;

    cin >> licz >> licz_bit;
    if (licz >= 0){
        string wyn = na_bin(licz, licz_bit);
        cout << wyn << endl;
    } else {
        string wyn_bewz = na_bin(licz * -1, licz_bit);
        string negacja = zamiana(wyn_bewz);
        string wyn = dodaj(negacja, licz_bit);
        cout << wyn << endl;
    }
    return 0;
}