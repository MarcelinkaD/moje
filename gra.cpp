#include<bits/stdc++.h>
typedef long long ll;
using namespace std;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int q;
    cin >> q;

    while(q--){
        int n, m;
        cin >> n >> m;
        vector<ll> a_przed;
        vector<ll> b_przed;
        vector<ll> a_po;
        vector<ll> b_po;
        vector<ll> przed;
        vector<ll> po;
        bool czy_byl_parz_a = false;
        bool czy_byl_parz_b = false;
        bool czy_byl_nieparz_a = false;
        bool czy_byl_nieparz_b = false;

        for (int i = 0; i < n; i++){
            ll x;
            cin >> x;
            a_przed.push_back(x);
            przed.push_back(x);
            if (x % 2 == 0){
                czy_byl_parz_a = true;
            } else {
                czy_byl_nieparz_a = true;
            }
        }
        for (int i = 0; i < m; i++){
            ll x;
            cin >> x;
            b_przed.push_back(x);
            przed.push_back(x);
            if (x % 2 == 0){
                czy_byl_parz_b = true;
            } else {
                czy_byl_nieparz_b = true;
            }
        }
        for (int i = 0; i < n; i++){
            ll x;
            cin >> x;
            a_po.push_back(x);
            po.push_back(x);
        }
        for (int i = 0; i < m; i++){
            ll x;
            cin >> x;
            b_po.push_back(x);
            po.push_back(x);
        }

        sort(przed.begin(), przed.end());
        sort(po.begin(), po.end());
        if (przed == po){
            bool wyn = true;
            for (int i = 0; i < n; i++){
                if (a_przed[i] == a_po[i]){
                    continue;
                }
                if (a_przed[i] % 2 == 0 && a_po[i] % 2 == 1){
                    wyn = false;
                    break;
                } else if (a_przed[i] % 2 == 1 && a_po[i] % 2 == 0){
                    wyn = false;
                    break;
                } else if (a_przed[i] % 2 == 1 && a_po[i] % 2 == 1 && czy_byl_nieparz_b == false) {
                    wyn = false;
                    break;
                } else if (a_przed[i] % 2 == 0 && a_po[i] % 2 == 0 && czy_byl_parz_b == false) {
                    wyn = false;
                    break;
                }
            }
            if (wyn){
                for (int i = 0; i < m; i++){
                    if (b_przed[i] == b_po[i]){
                        continue;
                    }
                    if (b_przed[i] % 2 == 0 && b_po[i] % 2 == 1){
                        wyn = false;
                        break;
                    } else if (b_przed[i] % 2 == 1 && b_po[i] % 2 == 0){
                        wyn = false;
                        break;
                    } else if (b_przed[i] % 2 == 1 && b_po[i] % 2 == 1 && czy_byl_nieparz_a == false) {
                        wyn = false;
                        break;
                    } else if (b_przed[i] % 2 == 0 && b_po[i] % 2 == 0 && czy_byl_parz_a == false) {
                        wyn = false;
                        break;
                    }
                }
            }
            if (wyn == false){
                cout << "NIE" << '\n';
            } else {
                cout << "TAK" << '\n';
            }
        } else {
            cout << "NIE" << '\n';
        }

    }

    return 0;
}