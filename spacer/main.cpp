#include <bits/stdc++.h>
using namespace std;

const int MAXN = 2e5 + 5;
//const int MAXN = 7;
vector<int> graf[MAXN];
unordered_set<int> sciezka1;
int poprzedni1[MAXN];
bool czy_odw[MAXN];

void bfs1(int pocz, int kon){
    queue<int> kol;
    kol.push(pocz);
    czy_odw[pocz] = true;
    poprzedni1[pocz] = -1;

    while (!kol.empty()){
        int akt_wie = kol.front();
        kol.pop();

        if (akt_wie == kon){
            return;
        }

        for (auto sasiad : graf[akt_wie]){
            if (!czy_odw[sasiad]){
                czy_odw[sasiad] = true;
                poprzedni1[sasiad] = akt_wie;
                kol.push(sasiad);
            }
        }
    }
}

bool czy_w_scie(int x){
    return sciezka1.find(x) != sciezka1.end();
}

void bfs2(int pocz, int kon){
    queue<int> kol;
    kol.push(pocz);
    czy_odw[pocz] = true;

    while (!kol.empty()){
        int akt_wie = kol.front();
        kol.pop();

        if (akt_wie != pocz && akt_wie != kon){
            if (czy_w_scie(akt_wie)){
                continue;
            }
        }

        for (auto sasiad : graf[akt_wie]){
            if (!czy_odw[sasiad]){
                //zle jesli sasiad jest w sciezce
                if ((sasiad == kon && akt_wie != pocz) || !czy_w_scie(sasiad)) {
                    kol.push(sasiad);
                    czy_odw[sasiad] = true;
                }
            }
        }
    }
}


int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    cin >> n >> m;
    int start, kon;
    cin >> start >> kon;

    for (int i = 0; i < m; i++){
        int a, b;
        cin >> a >> b;
        graf[a].push_back(b);
        graf[b].push_back(a);
    }

    bfs1(start, kon);
    int akt_wie = kon;
    while (akt_wie != -1){
        sciezka1.insert(akt_wie);
        akt_wie = poprzedni1[akt_wie];
    }

    for (int i = 0; i < MAXN; i++){
        czy_odw[i] = 0;
    }

    bfs2(kon, start);
    if (czy_odw[start] == false){
        cout << "NIE" << endl;
    } else {
        cout << "TAK" << endl;
    }

    return 0;
}
