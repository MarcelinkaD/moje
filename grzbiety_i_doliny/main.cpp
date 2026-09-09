//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/grz/18277/
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1005;
int graf[MAXN][MAXN];
bool czy_odw[MAXN][MAXN];
pair<int, int> ruchy[8] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}, {1, -1}, {-1, 1}, {1, 1}, {-1, -1}};

bool inRange(int i, int j, int n){
    if (i < n && j < n){
        return (-1 < i && -1 < j);
    }
    return 0;
}

int bfs(int i, int j, int n){
    queue<pair<int, int>> kol;
    kol.push({i, j});
    czy_odw[i][j] = 1;
    int wyn = -1; //-1 -> nie wiemy, 0 -> mix, 1 -> gora, 2 -> dolina
    while (!kol.empty()){
        pair<int, int> wie = kol.front();
        kol.pop();
        i = wie.first;
        j = wie.second;
        for (auto ruch : ruchy){
            int ni = i + ruch.first;
            int nj = j + ruch.second;
            if (inRange(ni, nj, n)){
                if (graf[ni][nj] == graf[i][j]){
                    if (!czy_odw[ni][nj]){
                        czy_odw[ni][nj] = 1;
                        kol.push({ni, nj});
                    }
                } else if (graf[ni][nj] < graf[i][j]){
                    if (wyn == -1 || wyn == 1){
                        wyn = 1;
                    } else {
                        wyn = 0;
                    }
                } else {
                    if (wyn == -1 || wyn == 2){
                        wyn = 2;
                    } else {
                        wyn = 0;
                    }
                }
            }
        }
    }
    return wyn;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            cin >> graf[i][j];
        }
    }

    int gory = 0;
    int doliny = 0;

    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            if (!czy_odw[i][j]){
                int wyn = bfs(i, j, n);
                if (wyn == 1){
                    gory++;
                } else if (wyn == 2){
                    doliny++;
                }
            }
        }
    }

    if (gory == 0 && doliny == 0){
        gory = 1;
        doliny = 1;
    }

    cout << gory << ' ' << doliny << endl;

    return 0;
}
