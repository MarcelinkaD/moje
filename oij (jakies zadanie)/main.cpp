//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/com/27566/
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 5005;
int wynik[MAXN][MAXN];
char tr[MAXN][MAXN];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    string s1, s2;
    cin >> s1 >> s2;
    int n = s1.size();
    int m = s2.size();

    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            if (s1[i] == s2[j]) {
                wynik[i + 1][j + 1] = wynik[i][j] + 1;
                tr[i + 1][j + 1] = 'o';
            } else if (wynik[i][j + 1] >= wynik[i + 1][j]) {
                wynik[i + 1][j + 1] = wynik[i][j + 1];
                tr[i + 1][j + 1] = 'i';
            } else {
                wynik[i + 1][j + 1] = wynik[i + 1][j];
                tr[i + 1][j + 1] = 'j';
            }
        }
    }

    cout << wynik[n][m] << '\n';
    string wyn = "";
    int i = n, j = m;
    while (i > 0 && j > 0) {
        if (tr[i][j] == 'o') {
            wyn += s1[i - 1];
            i--; j--;
        } else if (tr[i][j] == 'i') {
            i--;
        } else {
            j--;
        }
    }

    reverse(wyn.begin(), wyn.end());
    cout << wyn << endl;

    return 0;
}
