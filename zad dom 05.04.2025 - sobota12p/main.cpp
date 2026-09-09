//https://szkopul.edu.pl/problemset/problem/VZifqMhw2OhTWnQqv7mC5Cge/site/?key=statement
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 2005;
int wys[MAXN][MAXN];
stack<int> pop_kol;

int main()
{
    int n;
    cin >> n;

    for (int i = 1; i <= n; i++){
        for (int j = 1; j <= n; j++){
            int x;
            cin >> x;
            if (x == 0){
                wys[i][j] = wys[i - 1][j] + 1;
            } else {
                wys[i][j] = 0;
            }
        }
    }

    int max_wyn = -1;
    for (int i = 1; i <= n + 1; i++){
        for (int j = 1; j <= n + 1; j++){
            if (wys[i][j] > wys[i][j - 1]){
                pop_kol.push(wys[i][j]);
            } else {

            }
        }
    }

    return 0;
}
