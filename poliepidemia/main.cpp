#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1e5 + 5;
vector<int> graph[MAXN];
pair<int, int> dist[MAXN];

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;

    for (int i = 0; i < n - 1; i++) {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    queue<int> q;
    q.push(1);
    dist[1] = {0, 1};

    while (!q.empty()) {
        int new_ = q.front();
        q.pop();

        for (int edge : graph[new_]) {
            if (dist[edge].second == 0) {
                dist[edge].first = dist[new_].first + 1;
                dist[edge].second = 1;
                q.push(edge);
            }
        }
    }
    bool vis[n + 1];
    for (int i = 0; i <= n; i++)
    vis[i] = false;

    q.push(n);
    dist[n] = {0, 2};
    while (!q.empty()) {
        int new_ = q.front();
        q.pop();

        for (int edge : graph[new_]) {
            if (!vis[edge]) {
                if (dist[edge].first > dist[new_].first + 1) {
                    dist[edge].first = dist[new_].first + 1;
                    dist[edge].second = 2;
                }
                    vis[edge] = true;
                    q.push(edge);
                }
            }
    }

    int ligma = 0;
    int sigma = 0;
    for (int i = 0; i <= n; i++) {
        if (dist[i].second == 1)
            ligma++;
        else if (dist[i].second== 2)
            sigma++;
    }

    cout << (ligma > sigma ? "Ligma" : "Sugma");
}
