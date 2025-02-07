//https://szkopul.edu.pl/problemset/problem/Ak4wWPkNtHpF-OiulN1gixfW/site/?key=statement
/*#include <bits/stdc++.h>
using namespace std;

unordered_map<int, vector<int>> ind;

int binary(int licz, int akt_ind) {
    if (ind.find(licz) == ind.end()) {
        return -1;
    }
    int pocz = 0;
    int kon = ind[licz].size();
    while (pocz < kon) {
        int srodek = (pocz + kon) / 2;
        if (ind[licz][srodek] < akt_ind) {
            pocz = srodek + 1;
        } else {
            kon = srodek;
        }
    }

    if (pocz == (int)ind[licz].size()) {
        return -1;
    }

    if (ind[licz][pocz] >= akt_ind) {
        return ind[licz][pocz];
    }

    return -1;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;

    for (int i = 0; i < n; i++){
        int x;
        cin >> x;
        ind[x].push_back(i);
    }

    int q;
    cin >> q;

    for (int k = 0; k < q; k++){
        int m;
        cin >> m;
        string wynik = "TAK";
        int akt_ind = 0;
        for (int i = 0; i < m; i++){
            int akt_znak;
            cin >> akt_znak;
            int gdzie = binary(akt_znak, akt_ind);
            if (gdzie != -1){
                akt_ind = gdzie + 1;
            } else {
                wynik = "NIE";
            }
        }
        cout << wynik << endl;
    }

    return 0;
}*/

//https://szkopul.edu.pl/problemset/problem/AWhdD7i4V7mupdKWVtpgfGSM/site/?key=statement
#include <bits/stdc++.h>
using namespace std;

vector<int> l;
unordered_map<int, pair<int, int>> wyniki;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n, q;
    cin >> n >> q;

    for (int i = 0; i < n; i++){
        char x;
        cin >> x;
        if (x == 'T') {
            l.push_back(2);
        } else {
            l.push_back(1);
        }
    }

    for (int k = 0; k < q; k++){
        int s;
        cin >> s;
        if (wyniki.find(s) != wyniki.end()){
            cout << wyniki[s].first << ' ' << wyniki[s].second << endl;
        } else {
            int pocz, kon;
            pocz = 0;
            kon = 0;
            int akt_sum = 0;
            bool czy_break = false;
            while (kon < n) {
                while (pocz < n && akt_sum < s) {
                    akt_sum += l[pocz];
                    pocz++;
                    if (akt_sum == s) {
                        wyniki[s].first = kon + 1;
                        wyniki[s].second = pocz;
                        czy_break = true;
                        break;
                    }
                }
                if (czy_break) {
                    break;
                }
                akt_sum -= l[kon];
                kon++;
                if (akt_sum == s) {
                    wyniki[s].first = kon + 1;
                    wyniki[s].second = pocz;
                    czy_break = true;
                    break;
                }
            }
            if (czy_break) {
                cout << wyniki[s].first << ' ' << wyniki[s].second << endl;
            } else {
                cout << "NIE" << endl;
            }
        }
    }

    return 0;
}

