#include <bits/stdc++.h>
using namespace std;

unordered_map<char, int> tab_parz_1;
unordered_map<char, int> tab_parz_2;
unordered_map<char, int> tab_nieparz_1;
unordered_map<char, int> tab_nieparz_2;

int main()
{
    int n;
    cin >> n;

    string s1, s2;
    cin >> s1 >> s2;

    for (int i = 0; i < n; i += 2){
        tab_parz_1[s1[i]]++;
    }

    for (int i = 0; i < n; i += 2){
        tab_parz_2[s2[i]]++;
    }

    if (tab_parz_1 != tab_parz_2){
        cout << "NIE" << '\n';
        return 0;
    }

    for (int i = 1; i < n; i += 2){
        tab_nieparz_1[s1[i]]++;
    }

    for (int i = 1; i < n; i += 2){
        tab_nieparz_2[s2[i]]++;
    }

    if (tab_nieparz_1 != tab_nieparz_2){
        cout << "NIE" << '\n';
        return 0;
    }

    cout << "TAK" << '\n';

    return 0;
}
