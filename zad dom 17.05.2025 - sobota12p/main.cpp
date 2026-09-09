//https://www.spoj.com/problems/DQUERY/
#include <bits/stdc++.h>
using namespace std;

const int MAX_N = 30005;
const int MAX_A = 1000006;
const int MAX_Q = 200005;
const int SQRT = 170;

struct zap {
    int pocz, kon, nr;
};

int l[MAX_N];
int ile[MAX_A];
int odp[MAX_Q];
zap zapyt[MAX_Q];

int n, q;
int x = 1, y = 0;
int rozne = 0;

bool cmp(zap a, zap b) {
    int blokA = a.pocz / SQRT;
    int blokB = b.pocz / SQRT;
    if (blokA != blokB) {
        return blokA < blokB;
    }
    return a.kon < b.kon;
}

void dodaj(int i) {
    ile[l[i]]++;
    if (ile[l[i]] == 1) {
        rozne++;
    }
}

void usun(int i) {
    ile[l[i]]--;
    if (ile[l[i]] == 0){
        rozne--;
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> l[i];
    }

    cin >> q;
    for (int i = 1; i <= q; i++) {
        cin >> zapyt[i].pocz >> zapyt[i].kon;
        zapyt[i].nr = i;
    }

    sort(zapyt + 1, zapyt + 1 + q, cmp);

    for (int i = 1; i <= q; i++) {
        int l = zapyt[i].pocz;
        int r = zapyt[i].kon;

        while (x < l) {
            usun(x);
            x++;
        }
        while (x > l) {
            x--;
            dodaj(x);
        }
        while (y < r) {
            y++;
            dodaj(y);
        }
        while (y > r) {
            usun(y);
            y--;
        }

        odp[zapyt[i].nr] = rozne;
    }

    for (int i = 1; i <= q; i++) {
        cout << odp[i] << endl;
    }

    return 0;
}
