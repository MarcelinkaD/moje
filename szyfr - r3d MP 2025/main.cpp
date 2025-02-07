//https://szkopul.edu.pl/c/mistrz-programowania-2025/p/r3d/
#include <bits/stdc++.h>
typedef unsigned int ui;
using namespace std;

static const int BITS = 31;
struct WierzTrie {
    int dziecko[2];
    int ile_przechodzi;
    WierzTrie() {
        dziecko[0] = -1;
        dziecko[1] = -1;
        ile_przechodzi = 0;
    }
};

static const int MAXN = 300000;
static const int MAX_WIERZ = MAXN * (BITS + 1);
WierzTrie trie[MAX_WIERZ];
int wielkosc_trie = 1;

void wstawTrie(ui x){
    int wierz = 0;
    trie[wierz].ile_przechodzi++;
    for (int i = BITS - 1; i >= 0; i--){
        int bit = (x >> i) & 1U;
        if (trie[wierz].dziecko[bit] == -1) {
            trie[wierz].dziecko[bit] = wielkosc_trie++;
        }
        wierz = trie[wierz].dziecko[bit];
        trie[wierz].ile_przechodzi++;
    }
}

void usunTrie(ui x) {
    int wierz = 0;
    trie[wierz].ile_przechodzi--;
    for (int i = BITS - 1; i >= 0; i--) {
        int bit = (x >> i) & 1U;
        int nast = trie[wierz].dziecko[bit];
        wierz = nast;
        trie[wierz].ile_przechodzi--;
    }
}

ui znajdzMinXor(ui b) {
    int wierz = 0;
    ui x = 0;
    for (int i = BITS - 1; i >= 0; i--){
        int bit = (b >> i) & 1U;
        int preferowany = bit;
        if (trie[wierz].dziecko[preferowany] == -1 || trie[trie[wierz].dziecko[preferowany]].ile_przechodzi == 0){
            preferowany = 1 - preferowany;
        }
        x = (x << 1) | preferowany;
        wierz = trie[wierz].dziecko[preferowany];
    }
    return x;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;

    vector<ui> b(n), k(n);
    for (int i = 0; i < n; i++) {
        cin >> b[i];
    }

    for (int i = 0; i < n; i++) {
        cin >> k[i];
    }

    for (int i = 0; i < n; i++) {
        wstawTrie(k[i]);
    }

    vector<ui> a(n);
    for (int i = 0; i < n; i++){
        ui x = znajdzMinXor(b[i]);
        usunTrie(x);
        a[i] = b[i] ^ x;
    }

    for (int i = 0; i < n; i++){
        cout << a[i] << ' ';
    }

    return 0;
}
