#include <bits/stdc++.h>
using namespace std;

struct wierz {
    int dzieci[26];
    int id_str = -1;
    int max_dlu = 0;
    int glebokosc = 0;
    wierz() {
        fill_n(dzieci, 26, -1);
    }
};

vector<wierz> trie;
vector<string> napisy;
vector<int> kolejnosc;

void dodaj(string s, int ktory){
    int akt_wie = 0;
    for (auto akt_char : s){
        int ind = akt_char - 'a';
        if (trie[akt_wie].dzieci[ind] == -1){
            int nowy = (int)trie.size();
            trie[akt_wie].dzieci[ind] = nowy;
            trie.push_back(wierz());
            trie[nowy].glebokosc = trie[akt_wie].glebokosc + 1;
        }
        akt_wie = trie[akt_wie].dzieci[ind];
    }
    trie[akt_wie].id_str = ktory;
}

void ustal_dlugosc(){
    vector<int> kol;
    stack<int> stos;
    stos.push(0);
    while (!stos.empty()){
        int akt_wie = stos.top();
        stos.pop();
        kol.push_back(akt_wie);
        for (int i = 0; i < 26; i++){
            int sasiad = trie[akt_wie].dzieci[i];
            if (sasiad != -1){
                stos.push(sasiad);
            }
        }
    }

    for (int k = (int)kol.size() - 1; k >= 0; k--){
        int akt_wie = kol[k];
        int max_wyn;
        if (trie[akt_wie].id_str != -1){
            max_wyn = trie[akt_wie].glebokosc;
        } else {
            max_wyn = 0;
        }
        for (int i = 0; i < 26; i++){
            int sasiad = trie[akt_wie].dzieci[i];
            if (sasiad != -1){
                max_wyn = max(max_wyn, trie[sasiad].max_dlu);
            }
        }
        trie[akt_wie].max_dlu = max_wyn;
    }
}


void ustal_kolejnosc(){
    stack<int> stos;
    stos.push(0);
    while (!stos.empty()){
        int akt_wie = stos.top();
        stos.pop();
        if (trie[akt_wie].id_str != -1){
            kolejnosc.push_back(trie[akt_wie].id_str);
        }
        vector<pair<pair<int, int>, int>> sasiedzi;
        for (int i = 0; i < 26; i++){
            int sasiad = trie[akt_wie].dzieci[i];
            if (sasiad != -1){
                sasiedzi.push_back({{trie[sasiad].max_dlu, i}, sasiad});
            }
        }
        sort(sasiedzi.begin(), sasiedzi.end());
        for (int i = (int)sasiedzi.size() - 1; i >= 0; i--){
            stos.push(sasiedzi[i].second);
        }
    }
}

int pref(string s1, string s2){
    int wyn = 0;
    for (int i = 0; i < min(s1.size(), s2.size()); i++){
        if (s1[i] != s2[i]){
            break;
        }
        wyn++;
    }
    return wyn;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    trie.push_back(wierz());

    int n;
    cin >> n;
    napisy.resize(n);

    for (int i = 0; i < n; i++){
        cin >> napisy[i];
    }
    
    for (int i = 0; i < n; i++){
        dodaj(napisy[i], i);
    }

    ustal_dlugosc();
    ustal_kolejnosc();

    string wyn;
    for (auto znak : napisy[kolejnosc[0]]){
        wyn += znak;
    }
    wyn += 'E';

    string pop = napisy[kolejnosc[0]];
    string akt;
    for (int i = 1; i < n; i++){
        akt = napisy[kolejnosc[i]];
        int len_pop = pop.size();
        int len_akt = akt.size();
        int naj_pref = pref(pop, akt);
        int z = len_pop + len_akt - 2 * naj_pref + 2;
        int bez = len_akt + 1;
        if (z < bez){
            wyn += 'T';
            int zost = len_pop - naj_pref;
            for (int k = 0; k < zost; k++){
                wyn += 'B';
            }
            for (int k = naj_pref; k < len_akt; k++){
                wyn += akt[k];
            }
            wyn += 'E';
        } else {
            for (auto znak : akt){
                wyn += znak;
            }
            wyn += 'E';
        }
        pop = akt;
    }

    cout << wyn.size() << '\n';
    cout << wyn << '\n';
    return 0;
}