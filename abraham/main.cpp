//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/abr/
#include <bits/stdc++.h>
using namespace std;

vector<long long> kol;
vector<long long> prow;

int main()
{
    int n, m;
    cin >> n >> m;

    for (int i = 0; i < n; i++){
        long long x;
        cin >> x;
        kol.push_back(x);
    }

    for (int i = 0; i < m; i++){
        long long x;
        cin >> x;
        prow.push_back(x);
    }

    sort(kol.begin(), kol.end());
    sort(prow.begin(), prow.end());

    int i = 0;
    int j = 0;
    long long wyn = 0;
    while (i < n){
        if (j == m){
            cout << "NIE" << endl;
            cout << n - i << endl;
            return 0;
        }
        if (prow[j] <= kol[i]){
            j++;
        } else {
            wyn += prow[j] - kol[i];
            j++;
            i++;
        }
    }
    cout << "TAK" << endl;
    cout << wyn << endl;

    return 0;
}
