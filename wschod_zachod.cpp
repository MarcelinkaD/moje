#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, w, z;
    cin >> n >> w >> z;
    vector<vector<int>> graf(n);

    for (int i = 0; i < n - 1; i++){
        int a, b;
        cin >> a >> b;
        graf[a].push_back(b);
        graf[b].push_back(a);
    }
    
    int k;
    cin >> k;
    vector<int> gdzie(k);
    for (int i = 0; i < k; i++){
        int x;
        cin >> x;
        gdzie.push_back(x);
    }

    

    return 0;
}