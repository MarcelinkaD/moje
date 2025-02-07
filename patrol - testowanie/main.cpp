#include <bits/stdc++.h>
#include <random>
using namespace std;

int stworz_licz(int x, int dlu) {
    int w = 0;
    int pot = 1;
    for (int i = 0; i < dlu; i++){
        w += x * pot;
        pot *= 10;
    }
    return w;
}

int brut(string s)
{
    int akt = 1;
    int dlu = s.size();
    int si = stoi(s);

    while (true) {
        int akt_licz = stworz_licz(akt, dlu);
        if (akt_licz >= si) {
            return akt_licz;
        }
        akt++;
    }

    return 0;
}

int fast(string s)
{
    int dlu = s.size();
    if (dlu == 1) {
        return stoi(s);
    }

    bool czy_przerw = false;
    int zacz = s[0] - '0';
    for (int i = 1; i < dlu; i++){
        int x = s[i] - '0';
        int pop = s[i - 1] - '0';
        if (x > zacz) {
            zacz++;
            break;
        } else if (x < zacz) {
            break;
        }
    }

    if (zacz == 10) {
        zacz = 1;
        dlu++;
    }

    return stworz_licz(zacz, dlu);
}

int main()
{
    int akt_test = 1;
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> distrib(1, 100000);
    while (true) {
        int n = distrib(gen);
        string str = to_string(n);
        int w1 = brut(str);
        int w2 = fast(str);
        if (w1 == w2){
            cout << "Test " << akt_test << ": OK" << endl;
        } else {
            cout << "Test " << akt_test << ": BLAD" << endl;
            cout << "Brut: "<< w1 << endl;
            cout << "Fast: "<< w2 << endl;
            break;
        }
        akt_test++;
    }
    return 0;
}
