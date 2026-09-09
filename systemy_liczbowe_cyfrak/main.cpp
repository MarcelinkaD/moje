#include <fstream>
#include <bits/stdc++.h>
using namespace std;

bool czy_drugi_mniejszy(string x1, string x2){
    if (x1[0] == '-' && x2[0] != '-'){
        return false;
    }
    if (x1[0] != '-' && x2[0] == '-'){
        return true;
    }
    if (x1[0] == '-' && x2[0] == '-'){
        x1 = x1.substr(1, x1.size());
        x2 = x2.substr(1, x2.size());
    }
    if (x1.size() < x2.size()){
        return false;
    }
    if (x2.size() < x1.size()){
        return true;
    }

    for (int i = 0; i < x1.size(); i++){
        if (x1[i] == '1' && x2[i] == '0'){
            return true;
        }
        if (x1[i] == '0' && x2[i] == '0'){
            return false;
        }
    }
    return false;
}

string na_dwoj_z_dzies(int k, int ile){
    string w;
    while (k > 0){
        int reszta = k % 2;
        k /= 2;
        w = (char)(reszta + 48) + w;
    }
    return w;
}

string na_dwoj_z_czwor(string x){
    int n = x.size();
    string wyn;
    for (int i = n - 1; i >= 0; i--){
        if (x[i] == '-'){
            wyn = '-' + wyn;
            break;
        }
        wyn = na_dwoj_z_dzies(x[i] - 48, 2) + wyn;
    }
    return wyn;
}

int z_lit_na_licz(char x){
    if (x == 'A'){
        return 10;
    }
    if (x == 'B'){
        return 11;
    }
    if (x == 'C'){
        return 12;
    }
    if (x == 'D'){
        return 13;
    }
    if (x == 'E'){
        return 14;
    }
    if (x == 'F'){
        return 15;
    }
}

string na_dwoj_z_osem(string x){
    int n = x.size();
    string wyn;
    for (int i = n - 1; i >= 0; i--){
        if (x[i] == '-'){
            wyn = '-' + wyn;
            break;
        }
        if ((int)x[i] < 65) {
            wyn = na_dwoj_z_dzies(x[i] - 48, 3) + wyn;
        } else {
            wyn = na_dwoj_z_dzies(z_lit_na_licz(x[i]), 3) + wyn;
        }
    }
    return wyn;
}

int main()
{
    ifstream wej_dwoj("dane_systemy1.txt");
    ifstream wej_czwo("dane_systemy2.txt");
    ifstream wej_osem("dane_systemy3.txt");
    fstream wyj("wyniki_systemy.txt", ios::app);

    while (!wej_dwoj.eof()){

    }

    wej_dwoj.close();
    wej_czwo.close();
    wej_osem.close();
    wyj.close();
    return 0;
}
