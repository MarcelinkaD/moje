//https://sio2.mimuw.edu.pl/c/oi32-1/p/wal/
#include <bits/stdc++.h>
using namespace std;

struct robot {
    int s;
    int z;
};

robot robots[20];
bool czy_pokonany[20][20];
unsigned char cache[1 << 20];

bool eliminuj(int roboty, int n) {
    if(roboty == 0) return 1;
    if(cache[roboty] != 255) {
        return cache[roboty];
    }

    int pierw_rob = -1;
    for(int i = 0; i < n; i++) {
        if(roboty & (1 << i)) {
            pierw_rob = i;
            break;
        }
    }

    for (int j = pierw_rob + 1; j < n; j++) {
        if (roboty & (1 << j)) {
            bool pierw_rob_elim_j = czy_pokonany[pierw_rob][j];
            bool j_elim_pierw_rob = czy_pokonany[j][pierw_rob];

            int nowe_roboty = roboty;

            if(pierw_rob_elim_j) nowe_roboty &= ~(1 << j);
            if(j_elim_pierw_rob) nowe_roboty &= ~(1 << pierw_rob);

            if(eliminuj(nowe_roboty)) {
                return cache[roboty] = 1;
            }
        }
    }

    return cache[roboty] = 0;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> robots[i].s >> robots[i].z;
    }

    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++) {
            if (i == j) {
                czy_pokonany[i][j] = 0;
                continue;
            }
            if (roboty[i].s > roboty[j].s || roboty[i].z > roboty[j].z){
                czy_pokonany[i][j] = 1;
            } else {
                czy_pokonany[i][j] = 0;
            }
        }
    }

    memset(cache, 255, sizeof(cache));
    int roboty = (1 << n) - 1;

    if (eliminuj(roboty, n)) {
        cout << "TAK";
    } else {
        cout << "NIE";
    }
}
