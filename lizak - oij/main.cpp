//https://szkopul.edu.pl/problemset/problem/9y5Fywu8h7DyO89-gd5ifrju/site/?key=statement
#include <bits/stdc++.h>
using namespace std;

map<int, vector<int>> wyst;
const int INF = 1e9 + 7;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    int min_wyn = INF;
    int akt_wyn;
    for (int i = 0; i < n; i++){
        int x;
        cin >> x;
        if (wyst.find(x) == wyst.end()){
            wyst[x] = {};
            wyst[x].push_back(i);
        } else {
            if (wyst[x].size() < 2){
                wyst[x].push_back(i);
            } else {
                wyst[x].push_back(i);
                int akt_size = wyst[x].size();
                akt_wyn = wyst[x][akt_size - 1] - wyst[x][akt_size - 3] + 1;
                min_wyn = min(min_wyn, akt_wyn);
            }
        }
    }

    if (min_wyn == INF){
        cout << "NIE" << endl;
    } else {
        cout << min_wyn << endl;
    }

    return 0;
}
