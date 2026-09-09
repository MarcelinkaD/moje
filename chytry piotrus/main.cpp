#include <bits/stdc++.h>
using namespace std;

vector<int> l1;
vector<int> l2;
const int MAXN = 1e5 + 5;
bool czy_bylo[MAXN];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    for (int i = 0; i < n; i++){
        int a, b;
        cin >> a >> b;
        l1.push_back(a);
        l2.push_back(b);
    }

    sort(l1.begin(), l1.end());
    sort(l2.begin(), l2.end());

    int wyn = 0;
    int i = 0;
    int k = 0;
    int wyk = 0;
    while (i < n){
        if (czy_bylo[k] == 1) continue;
        if (l1[i] == l2[k]){
            k++;
        } else {
            wyn += abs(l1[i] - l2[k]);
            czy_bylo[k] = 1;
            wyk++;
            i++;
            k++;
        }
        if (k == n && wyk != n){
            k = 0;
        }
    }

    cout << wyn << endl;

    return 0;
}
