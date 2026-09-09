//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/kza/
#include <bits/stdc++.h>
using namespace std;

map<int, pair<int, int>> wyst;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;

    int min_wyn = 1e9;
    int max_wyn = 0;
    for (int i = 0; i < n; i++){
        int x;
        cin >> x;
        if (wyst.find(x) == wyst.end()){
            wyst[x].first = i;
            wyst[x].second = i;
        } else {
            min_wyn = min(min_wyn, i - wyst[x].second);
            max_wyn = max(max_wyn, i - wyst[x].first);
            wyst[x].second = i;
        }
    }

    if (min_wyn == 1e9){
        min_wyn = 0;
    }

    cout << min_wyn << ' ' << max_wyn;

    return 0;
}
