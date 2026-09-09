#include <bits/stdc++.h>
using namespace std;

struct wierz {
    int dzieci[26];
    int id_str = -1;
    int glebokosc = 0;
    wierz() { memset(dzieci, -1, sizeof(dzieci)); }
};

vector<wierz> trie;

void dodaj(string s, int ktory){
    int akt_wie = 0;
    for (auto akt_char : s){
        int ind = akt_char - 'a';
        int &nast = trie[akt_wie].dzieci[ind];
        if (nast == -1){
            nast = (int)trie.size();
            trie.push_back(wierz());
            trie[nast].glebokosc = trie[akt_wie].glebokosc + 1;
        }
        akt_wie = nast;
    }
    trie[akt_wie].id_str = ktory;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    trie.push_back(wierz());

    int n;
    cin >> n;

    for (int i = 0; i < n; i++){
        string x;
        cin >> x;
        dodaj(x, i);
    }

    return 0;
}