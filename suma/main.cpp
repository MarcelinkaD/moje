//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/sum1/
//drzewo punkt-przedzial
#include <bits/stdc++.h>
using namespace std;

const int R = (1 << 20);
long long drzewo[R * 2];
long long przep[R * 2];

void przepchniecie(int akt_wie, int roz){
    if (przep[akt_wie] != 0){
        drzewo[akt_wie * 2] += przep[akt_wie] * (roz / 2);
        drzewo[akt_wie * 2 + 1] += przep[akt_wie] * (roz / 2);
        przep[akt_wie * 2] += przep[akt_wie];
        przep[akt_wie * 2 + 1] += przep[akt_wie];
        przep[akt_wie] = 0;
    }
}

void dodaj(int akt_wie, int pocz_odp, int kon_odp, int pocz_pyt, int kon_pyt, long long war){
    int rozmiar_przed = kon_odp - pocz_odp + 1;
    if (pocz_pyt <= pocz_odp && kon_odp <= kon_pyt){
        drzewo[akt_wie] += war * rozmiar_przed;
        przep[akt_wie] += war;
        return;
    }

    if (kon_odp < pocz_pyt || pocz_odp > kon_pyt){
        return;
    }

    int srodek = (pocz_odp + kon_odp) / 2;
    przepchniecie(akt_wie, rozmiar_przed);
    dodaj(akt_wie * 2, pocz_odp, srodek, pocz_pyt, kon_pyt, war);
    dodaj(akt_wie * 2 + 1, srodek + 1, kon_odp, pocz_pyt, kon_pyt, war);
    drzewo[akt_wie] = drzewo[akt_wie * 2] + drzewo[akt_wie * 2 + 1];
}

long long znajdz(int akt_wie, int pocz_odp, int kon_odp, int poz){
    if (pocz_odp == kon_odp){
        return drzewo[akt_wie];
    }
    int srodek = (pocz_odp + kon_odp) / 2;
    przepchniecie(akt_wie, kon_odp - pocz_odp + 1);
    if (poz <= srodek){
        return znajdz(akt_wie * 2, pocz_odp, srodek, poz);
    } else {
        return znajdz(akt_wie * 2 + 1, srodek + 1, kon_odp, poz);
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    for (int i = 0; i < n; i++){
        cin >> drzewo[i + R];
    }

    for (int i = R - 1; i >= 1; i--){
        drzewo[i] = drzewo[2 * i] + drzewo[2 * i + 1];
    }

    for (int i = 0; i < m; i++){
        int typ, a, b, c;
        cin >> typ;
        if (typ == 2){
            cin >> a >> b >> c;
            dodaj(1, 0, R - 1, a - 1, b - 1, c);
        } else {
            cin >> a;
            cout << znajdz(1, 0, R - 1, a - 1) << '\n';
        }
    }

    return 0;
}
