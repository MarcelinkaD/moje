#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1000005;
//const int MAXN = 7;
int wyn[MAXN];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    for (int i = 0; i < MAXN; i++){
        wyn[i] = -1;
    }

    string s1;
    string s2;

    cin >> s1 >> s2;

    int n = s1.size();
    int m = s2.size();
    for (int i = n - 1; i >= 0; i--){
        for (int j = m - 1; j >= 0; j--){
            int akt_cyfra_s1 = s1[i] - '0';
            int akt_cyfra_s2 = s2[j] - '0';
            int iloczyn = akt_cyfra_s1 * akt_cyfra_s2;
            int cyfra = iloczyn % 10;
            int przechodzi = iloczyn / 10;
            int akt_ind = (n - i - 1) + (m - j - 1);
            if (wyn[akt_ind] == -1){
                wyn[akt_ind] = 0;
            }
            wyn[akt_ind] += cyfra;
            if (wyn[akt_ind + 1] == -1 && przechodzi != 0){
                wyn[akt_ind + 1] = 0;
            }
            wyn[akt_ind + 1] += przechodzi;
        }
    }

    for (int i = 0; i < MAXN; i++){
        if (wyn[i] >= 10){
            int przechodzi = wyn[i] / 10;
            int zostaje = wyn[i] % 10;
            if (wyn[i + 1] == -1){
                wyn[i + 1] = 0;
            }
            wyn[i] = zostaje;
            wyn[i + 1] += przechodzi;
        }
    }

    int kon = -1;
    int i = 0;
    while (wyn[i] != -1) {
        i++;
    }
    kon = i - 1;

    for (int i = kon; i >= 0; i--){
        cout << wyn[i];
    }

    return 0;
}
