//https://szkopul.edu.pl/c/mistrz-programowania-2025/p/r5c/
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1e6 + 4;
int wyn[MAXN];
vector<int> l;

bool czyGit(int n) {
    if (wyn[n - 1] < 0) {
        return false;
    }

    for (int i = 0; i < n - 1; i++){
        if (i < 0 || wyn[i] + wyn[i + 1] != l[i]) {
            return false;
        }
    }
    return true;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;

    for (int i = 0; i < n - 1; i++) {
        int x;
        cin >> x;
        wyn[i] = -1;
        wyn[i + 1] = -1;
        l.push_back(x);
    }

    for (int i = 0; i < n - 1; i++){
        if (l[i] == 0) {
            wyn[i] = 0;
            wyn[i + 1] = 0;
        } else {
            if (wyn[i] == 0){
                wyn[i + 1] = l[i];
            } else if (wyn[i] == -1){
                if (i + 1 == n - 1 || l[i + 1] != 0) {
                    wyn[i] = 1;
                    wyn[i + 1] = l[i] - 1;
                } else {
                    wyn[i] = l[i];
                }
            } else {
                wyn[i + 1] = l[i] - wyn[i];
            }
        }
    }

    bool pop = czyGit(n);
    if (pop) {
        cout << "Tak" << endl;
        for (int i = 0; i < n; i++){
            int s = wyn[i];
            cout << s << ' ';
        }
    } else {
        cout << "Nie" << endl;
    }

    return 0;
}
