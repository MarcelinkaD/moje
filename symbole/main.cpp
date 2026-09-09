#include <bits/stdc++.h>
#include <fstream>
using namespace std;

string zmien(string s){
    string w;
    for (auto c : s){
        if (c == '*'){
            w += '2';
        }
        if (c == '+'){
            w += '1';
        }
        if (c == 'o'){
            w += '0';
        }
    }
    return w;
}

int trzy_na10(string x){
    int w = 0;
    for (auto c : x){
        int licz = c - 48;
        w *= 3;
        w += licz;
    }
    return w;
}

string zmiana(string s){
    string w;
    for (auto c : s){
        if (c == '2'){
            w += '*';
        }
        if (c == '1'){
            w += '+';
        }
        if (c == '0'){
            w += 'o';
        }
    }
    return w;
}

string dzies_na3(int x){
    string wyn;
    while (x > 0){
        int reszta = x % 3;
        char znak = (reszta + 48);
        wyn = znak + wyn;
        x /= 3;
    }
    return zmiana(wyn);
}

int main(){
    fstream wej, wyj;
    wej.open("symbole.txt", ios::in);
    wyj.open("wynik.txt", ios::out);

    int max1 = -1;
    string wyn1;
    int suma = 0;
    while (!wej.eof()){
        string s;
        wej >> s;
        int dzies = trzy_na10(zmien(s));
        if (max1 < dzies){
            max1 = dzies;
            wyn1 = s;
        }
        suma += dzies;
    }

    string wyn2 = dzies_na3(suma);
    wyj << max1 << ' ' << wyn1 << '\n';
    wyj << suma << ' ' << wyn2 << '\n';
    wej.close();
    wyj.close();
    return 0;
}