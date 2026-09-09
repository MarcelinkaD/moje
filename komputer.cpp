#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int licz_prob;
    cin >> licz_prob;
    string a, b;
    cin >> a >> b;
    int n = a.size();
    int m = b.size();
    int ile_x = 0;
    int ile_y = 0;

    for (auto i : a){
        if (i == 'X'){
            ile_x++;
        } else {
            ile_y++;
        }
    }

    vector<pair<int, int>> wyn;
    for (int l1 = 1; l1 <= m / ile_x; l1++){
        ll pierw = (ll)ile_x * l1;
        if (pierw > m){
            break;
        }
        ll zost = m - pierw;
        if (zost % ile_y != 0){
            continue;
        }
        int l2 = zost / ile_y;
        if (l2 < 1){
            continue;
        }
    
        string ax, ay;
        bool fx = true, fy = true;
        int ind = 0;
        bool czy_git = true;
        for (auto znak : a){
            int dlu;
            if (znak == 'X'){
                dlu = l1;
            } else {
                dlu = l2;
            }
            if (ind + dlu > m){
                czy_git = false;
                break;
            }
            string seg = b.substr(ind, dlu);
            if (znak == 'X') {
                if (fx) {
                    ax = seg;
                    fx = false;
                } else if (seg != ax) {
                    czy_git = false;
                    break;
                }
            } else {
                if (fy) {
                    ay = seg;
                    fy = false;
                } else if (seg != ay) {
                    czy_git = false;
                    break;
                }
            }
            ind += dlu;
        }
        if (!czy_git || ind != m) {
            continue;
        }
        if (ax == ay) continue;
        wyn.push_back({l1, l2});
    }
    sort(wyn.begin(), wyn.end());
    int ile = wyn.size();
    if (ile > licz_prob) {
        cout << ":(" << " " << ile << endl;
    } else {
        cout << ile << endl;
        for (auto p : wyn) {
            cout << p.first << " " << p.second << endl;
        }
    }
    return 0;
}
