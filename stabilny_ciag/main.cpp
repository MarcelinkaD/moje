//AleMozgi 2024/2025
#include <bits/stdc++.h>
using namespace std;

vector<int> l;
unordered_map<int, int> max_dl;

bool znajdz(int x){
    if (max_dl.find(x) != max_dl.end()){
        return 1;
    }
    return 0;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    for (int i = 0; i < n; i++){
        int x;
        cin >> x;
        l.push_back(x);
    }

    int max_wyn = 0;
    for (int i = 0; i < n; i++){
        int akt_dl = 0;
        if (znajdz(l[i] - 1)){
            if (akt_dl < max_dl[l[i] - 1]){
                akt_dl = max_dl[l[i] - 1];
            }
        }
        if (znajdz(l[i])){
            if (akt_dl < max_dl[l[i]]){
                akt_dl = max_dl[l[i]];
            }
        }
        if (znajdz(l[i] + 1)){
            if (akt_dl < max_dl[l[i] + 1]){
                akt_dl = max_dl[l[i] + 1];
            }
        }
        max_dl[l[i]] = akt_dl + 1;
        max_wyn = max(max_wyn, max_dl[l[i]]);
    }

    cout << max_wyn << endl;

    return 0;
}
