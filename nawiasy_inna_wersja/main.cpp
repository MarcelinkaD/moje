//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/naw/
#include <bits/stdc++.h>
using namespace std;

map<char, char> dopasowanie = {{'{', '}'}, {'[', ']'}, {'(', ')'}};
set<char> otwarte = {'[', '{', '('};

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie();

    int q;
    cin >> q;

    for (int k = 0; k < q; k++){
        string s;
        cin >> s;
        stack<char> stos;
        bool odp = true;
        for (auto nawias : s){
            if (otwarte.find(nawias) != otwarte.end()){
                stos.push(nawias);
            } else if (!stos.empty()){
                char akt = stos.top();
                if (dopasowanie[akt] == nawias){
                    stos.pop();
                } else {
                    odp = false;
                    break;
                }
            } else {
                odp = false;
                break;
            }
        }
        if (odp && stos.empty()){
            cout << "TAK" << endl;
        } else {
            cout << "NIE" << endl;
        }

    }

    return 0;
}
