#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

bool czy_literka(char x){
    return (x >= 'a' && x <= 'z') || (x >= 'A' && x <= 'Z');
}

char szyfr(char c, int ile){
    if (c >= 'A' && c <= 'Z') {
        int nc = c + ile;
        if (nc > 'Z') {
            nc -= 26;
        } 
        return char(nc);
    }
    if (c >= 'a' && c <= 'z') {
        int nc = c + ile;
        if (nc > 'z') {
            nc -= 26;
        }
        return char(nc);
    }
    return c;
}

int przesuniecie(string x){
    unordered_set<string> jakie = {"caluje", "zawsze", "Twoj", "Kodus"};
    for (int i = 0; i <= 25; i++){
        string ns;
        for (auto znak : x){
            ns += szyfr(znak, i);
        }
        if (jakie.find(ns) != jakie.end()){
            return i;
        }
    }
    return -1;
}

string przesun(string s, int ile){
    string ns;
    for (auto znak : s){
        if (czy_literka(znak)){
            ns += szyfr(znak, ile);
        } else {
            ns += znak;
        }
    }
    return ns;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int q;
    cin >> q;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    while (q--){
        string s;
        getline(cin, s); 

        string akt_slowo;
        for (auto znak : s){
            if (czy_literka(znak)){
                akt_slowo += znak;
            } else {
                int wyn = przesuniecie(akt_slowo);
                if (wyn != -1){
                    cout << przesun(s, wyn) << '\n';
                    break;
                }
                akt_slowo.clear();
            }
        }
    }

    return 0;
}