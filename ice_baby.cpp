#include <bits/stdc++.h>
using namespace std;

int main(){ 
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int q;
    cin >> q;
    while (q--){
        int n;
        cin >> n;
        multiset<int> prze;
        prze.emplace(0);
        for (int i = 0; i < n; i++){
            int a, b;
            cin >> a >> b;
            auto gdzie = prze.upper_bound(b);
            if (gdzie != prze.end()){
                prze.erase(gdzie);
            }
            prze.insert(a);
            cout << (int)prze.size() - 1 << ' ';
        }
        cout << endl;
    }

    return 0;
}