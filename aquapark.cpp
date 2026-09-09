#include <bits/stdc++.h>
using namespace std;

int akt_pol[2005][2005];
long long sumy[2005][2005];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, q;
    cin >> n >> q;

    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            int x;
            cin >> x;
            akt_pol[i - j + n][i + j + 1] = x;
        }
    }

    for (int i = 1; i <= 2*n - 1; i++){
        for (int j = 1; j <= 2*n - 1; j++){
            sumy[i][j] = sumy[i - 1][j] + sumy[i][j - 1] - sumy[i - 1][j - 1] + akt_pol[i][j];
        }
    }

    while (q--){
        int i, j, k;
        cin >> i >> j >> k;
        int ni = i - j + n; 
        int nj = i + j - 1; 
        int ki = min(2*n - 1, ni + k);
        int kj = min(2*n - 1, nj + k);
        int pi = max(1, ni - k);
        int pj = max(1, nj - k);
        
        long long wyn = sumy[ki][kj] - sumy[ki][pj - 1] - sumy[pi - 1][kj] + sumy[pi - 1][pj - 1];
        cout << wyn << '\n';
    }

    return 0;
}
