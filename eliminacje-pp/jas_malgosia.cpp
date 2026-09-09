    #include <bits/stdc++.h>
    #define ll long long
    using namespace std;

    struct kraw {
        int wierz;
        ll droga;
    };

    vector<vector<kraw>> graf;
    vector<pair<ll, ll>> odl;
    unordered_set<int> zakazane;

    void bfs(int start, int end){
        queue<int> kol;
        kol.push(start);
        odl.at(start).second = 0;
        while(!kol.empty()){
            int u = kol.front();
            kol.pop();
            

            for (auto sasiad : graf.at(u)){
                if (odl.at(sasiad.wierz).second == -1 && zakazane.find(sasiad.wierz) == zakazane.end()){
                    odl.at(sasiad.wierz).second = odl.at(u).second + 1;
                    kol.push(sasiad.wierz);
                }
            }
            if (u == end) {
                return;
            }
        }
    }

    void dijkstra(int start){
        priority_queue<pair<ll, int>> q;
        odl.at(start).first = 0;
        odl.at(start).second = 0;
        q.push({0, start});
        while (!q.empty()) {
            pair<ll, int> v = q.top();
            q.pop();
            
            for (auto sasiad : graf.at(v.second)){
                if (zakazane.find(sasiad.wierz) == zakazane.end()){
                    if (odl.at(sasiad.wierz).first == -1 || odl.at(sasiad.wierz).first > odl.at(v.second).first + sasiad.droga){
                        odl.at(sasiad.wierz).first = odl.at(v.second).first + sasiad.droga;
                        odl.at(sasiad.wierz).second = odl.at(v.second).second + 1;
                        q.push({odl.at(sasiad.wierz).first, sasiad.wierz});
                    }
                }
            }
        }
    }

    int main(){
        ios_base::sync_with_stdio(0);
        cin.tie(0);

        int n, m;
        cin >> n >> m;
        graf.resize(n + 1);
        odl.resize(n + 1);
        for (int i = 0; i < n + 1; i++)
            odl[i] = {-1, -1};
        
        for (int i = 0; i < m; i++){
            int a, b, c;
            cin >> a >> b >> c;
            kraw k;
            k.droga = c;
            k.wierz = b;
            kraw k2;
            k2.droga = c;
            k2.wierz = a;
            graf.at(a).push_back(k);
            graf.at(b).push_back(k2);
        }

        int q;
        cin >> q;
        while (q--){
            int t;
            cin >> t;
            for (int i = 0; i < t; i++){
                int x;
                cin >> x;
                zakazane.insert(x);
            }
            int a, b;
            cin >> a >> b;
            for (int i = 0; i < n + 1; i++)
                odl[i] = {-1, -1};
            bfs(a, b);
            int odl_bfs = odl.at(b).second;
            for (int i = 0; i < n + 1; i++)
                odl[i] = {-1, -1};
            dijkstra(a);
            int odl_dijkstra = odl.at(b).second;
            if (odl_bfs == -1) {
                cout << "NO\n";
                zakazane.clear();
                continue;
            }
            if (odl_bfs == odl_dijkstra) {
                cout << "YES" << '\n';
            } else {
                cout << "NO" << '\n';
            }
            zakazane.clear();
        }

        return 0;
    }