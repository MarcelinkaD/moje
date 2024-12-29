//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/prz1/
#include <iostream>
#include <vector>
#include <stack>
using namespace std;

const int MAXN = 105;
vector<int> graf[MAXN];
vector<int> graftra[MAXN];
int ktora_grupa[MAXN];
int sss[MAXN];
stack<int> stos;

void DFS(int v, int akt_zna){
    ktora_grupa[v] = akt_zna;
    for (int i = 0; i < graf[v].size(); i++) {
        int sasiad = graf[v][i];
        if (ktora_grupa[sasiad] == 0) {
            DFS(sasiad, akt_zna);
        }
    }
    stos.push(v);
}

void DFS2(int v, int akt_zna){
    sss[v] = akt_zna;
    for (int i = 0; i < graftra[v].size(); i++) {
        int sasiadT = graftra[v][i];
        if (ktora_grupa[v] == ktora_grupa[sasiadT] && sss[sasiadT] == 0) {
            DFS2(sasiadT, akt_zna);
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int q;
    cin >> q;

    while (q) {
        int n;
        cin >> n;

        for (int i = 1; i <= n; i++) {
            graf[i].clear();
            graftra[i].clear();
            ktora_grupa[i] = 0;
            sss[i] = 0;
        }

        while (!stos.empty()) stos.pop();

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                char x;
                cin >> x;
                if (x == 'Y'){
                    graf[i].push_back(j);
                    graftra[j].push_back(i);
                }
            }
        }

        for (int i = 1; i <= n; i++){
            if (ktora_grupa[i] == 0){
                DFS(i, i);
            }
        }

        int w = 0;
        while (!stos.empty()) {
            int u = stos.top();
            stos.pop();
            if (sss[u] == 0) {
                w++;
                DFS2(u, w);
            }
        }
        cout << w << endl;
        q--;
    }

    return 0;
}
