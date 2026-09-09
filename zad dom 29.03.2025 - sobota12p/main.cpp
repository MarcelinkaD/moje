//https://szkopul.edu.pl/problemset/problem/deIZtcberd8cAXH64zlIq0wC/site/?key=statement
#include "cliclib.h"
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

ll akt_stawka = 1;
ll stos = 0;
ll po_trzy, po_dwa;
ll baj;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    ll n = inicjuj();

    while (true){
        po_trzy = akt_stawka * 3;
        po_dwa = akt_stawka * 2;

        if (akt_stawka + stos >= n){
            alojzy(1);
            break;
        }

        if (po_trzy + stos >= n){
            alojzy(3);
            akt_stawka = po_trzy;
        } else if (po_trzy * 3 + stos >= n){
            if (po_dwa * 3 + stos < n){
                alojzy(2);
                akt_stawka *= 2;
            } else {
                alojzy(1);
                akt_stawka = 1;
                stos += akt_stawka;
            }
        } else {
            alojzy(3);
            akt_stawka *= 3;
        }

        baj = bajtazar();

        if (baj == 1){
            stos += akt_stawka;
            akt_stawka = 1;
        } else {
            akt_stawka *= baj;
        }

    }

    return 0;
}
