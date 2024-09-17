#include <iostream>
#include <vector>
using namespace std;

bool in_Range (int i, int k, int n) {
    return (-1 < i && i < n) && (-1 < k && k < n);
}

int main()
{
    int n;
    cin >> n;
    vector<vector<int>> sumy(n, vector<int>(n));

    for (int i = 0; i < n; i++) {
        for (int k = 0; k < n; k++) {
            char znak;
            cin >> znak;

            if (znak == 48) {
                sumy[i][k] = 0;
            } else {
                sumy[i][k] = 1;
            }
        }
    }

    int wynik = 0;

    for (int i = n - 1; i >= 0; i--) {
        for (int k = 0; k < n; k++) {
            if (sumy[i][k] >= 1) {
                if (in_Range(i + 1, k - 1, n) && in_Range(i + 1, k + 1, n) && sumy[i + 1][k] >= 1) {
                    sumy[i][k] = 1 + min(sumy[i + 1][k - 1], sumy[i + 1][k + 1]);
                }
                wynik += sumy[i][k];
            }
        }
    }

    cout << wynik;

    return 0;
}
