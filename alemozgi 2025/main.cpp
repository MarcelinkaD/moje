//Wakacje
/*#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, a, b;
    cin >> n >> a >> b;

    for (int i = 1; i <= n; i++){
        if (i >= a && i <= b){
            cout << 'W';
        } else {
            cout << '.';
        }
    }
    return 0;
}
*/

//Podzielne 3
/*#include <bits/stdc++.h>
using namespace std;

int zlicz_reszty[3] = {0};

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    for (int i = 0; i < n; i++){
        int x;
        cin >> x;
        zlicz_reszty[x % 3]++;
    }

    int c0 = zlicz_reszty[0];
    int c1 = zlicz_reszty[1];
    int c2 = zlicz_reszty[2];

    int osobno = c0;
    int pary = min(c1, c2);
    int poz_c1 = max(c1 - c2, 0);
    int poz_c2 = max(c2 - c1, 0);
    int trojki = (poz_c1 / 3) + (poz_c2 / 3);

    int wyn = osobno + pary + trojki;
    cout << wyn << endl;

    return 0;
}
*/

//Pileczki
/*#include <bits/stdc++.h>
using namespace std;

unordered_map<char, vector<int>> zlicz;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    for (int i = 0; i < n; i++){
        string x;
        cin >> x;
        char lit = x[0];
        zlicz[lit].push_back(x[1] - '0');
    }

    int wyn = 0;
    for (char lit = 'A'; lit <= 'Z'; lit++){
        if (zlicz.find(lit) != zlicz.end()){
            sort(zlicz[lit].begin(), zlicz[lit].end());
            int pop = 0;
            int akt_wyn = 0;
            for (int i = 0; i < zlicz[lit].size(); i++) {
                if (i == 0){
                    akt_wyn++;
                } else if (zlicz[lit][i] == pop + 1){
                    akt_wyn++;
                } else if (zlicz[lit][i] == pop){
                    continue;
                } else {
                    wyn = max(wyn, akt_wyn);
                    akt_wyn = 1;
                }
                pop = zlicz[lit][i];
            }
            wyn = max(wyn, akt_wyn);
        }
    }

    cout << wyn << endl;

    return 0;
}*/


//Gluchy telefon
#include <bits/stdc++.h>
using namespace std;

vector<int> graf;
vector<int> stan_odw;
vector<int> sciezka;
vector<bool> czy_w_cyklu;

void dfs(int akt){
    stan_odw[akt] = 1;
    sciezka.push_back(akt);
    int nast = graf[akt];
    if (stan_odw[nast] == 0){
        dfs(nast);
    } else if (stan_odw[nast] == 1){
        int ind = (int)sciezka.size() - 1;
        while (ind >= 0 && sciezka[ind] != nast){
            czy_w_cyklu[sciezka[ind]] = 1;
            ind--;
        }
        if (ind >= 0){
            czy_w_cyklu[sciezka[ind]] = 1;
        }
    }
    stan_odw[akt] = 2;
    sciezka.pop_back();
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    graf.resize(n + 1);
    stan_odw.resize(n + 1, 0);
    czy_w_cyklu.resize(n + 1, false);

    for (int i = 0; i < n; i++){
        int x;
        cin >> x;
        graf[i + 1] = x;
    }

    for (int i = 1; i <= n; i++){
        if (stan_odw[i] == 0){
            dfs(i);
        }
    }

    for (int i = 1; i <= n; i++) {
        if (czy_w_cyklu[i]) {
            cout << i << ' ';
        }
    }
    cout << endl;

    return 0;
}


//Kino
/*#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1e5 + 5;
int prefix[MAXN][26];
int sufix[MAXN][26];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    string s;
    cin >> s;
    int n = s.size();

    for (int i = 1; i <= n; i++){
        for (char lit = 'A'; lit <= 'Z'; lit++){
            int ind = lit - 'A';
            prefix[i][ind] = prefix[i - 1][ind];
        }
        prefix[i][s[i] - 'A']++;
    }

    for (int i = n - 1; i >= 0; i--){
        for (char lit = 'A'; lit <= 'Z'; lit++){
            int ind = lit - 'A';
            sufix[i][ind] = sufix[i + 1][ind];
        }
        sufix[i][s[i] - 'A']++;
    }

    int wyn = 0;
    for (int k = 1; k <= n; k++) {
        int max_pre = 0;
        for (int i = 0; i < 26; i++) {
            max_pre = max(max_pre, prefix[k][i]);
        }
        int max_suf = 0;
        for (int i = 0; i < 26; i++) {
            max_suf = max(max_suf, sufix[k][i]);
        }
        wyn = max(wyn, max_pre + max_suf);
    }

    cout << wyn << endl;

    return 0;
}*/


//Kamienie
/*#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

const ll INF = LLONG_MAX;
vector<ll> koszt;
vector<ll> dp;
deque<ll> dq;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, a, b;
    cin >> n >> a >> b;

    koszt.resize(n);
    dp.resize(n, INF);
    for (int i = 0; i < n; i++){
        cin >> koszt[i];
    }

    dp[0] = koszt[0];
    dq.push_back(0);
    for (int i = 1; i < n; i++){
        while (!dq.empty() && dq.front() < i - b){
            dq.pop_front();
        }

        if (!dq.empty() && dq.front() <= i - a){
            dp[i] = koszt[i] + dp[dq.front()];
        }

        if (dp[i] != INF) {
            while (!dq.empty() && dp[dq.back()] >= dp[i])
                dq.pop_back();
            dq.push_back(i);
        }
    }

    if (dp[n - 1] != INF){
        cout << dp[n - 1] << endl;
    } else {
        cout << "BRAK" << endl;
    }

    return 0;
}

*/
//Unikalne
/*#include <bits/stdc++.h>
using namespace std;

vector<int> l;
unordered_set<int> uzyte;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    l.resize(n);
    for (int i = 0; i < n; i++){
        cin >> l[i];
    }

    sort(l.begin(), l.end());

    for (int x : l) {
        if (uzyte.find(x - 2) == uzyte.end()){
            uzyte.insert(x - 2);
        }
        else if (uzyte.find(x) == uzyte.end()){
            uzyte.insert(x);
        }
        else if (uzyte.find(x + 2) == uzyte.end()){
            uzyte.insert(x + 2);
        }
    }

    cout << uzyte.size() << endl;
    return 0;
}
*/
