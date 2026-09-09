//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/tem/
#include <bits/stdc++.h>
using namespace std;

vector<pair<int, int>> l;
deque<pair<int, int>> kol;

void wstaw(int x){
    int ile = 0;
    while (!kol.empty() && kol.back().first <= x){
        ile += kol.back().second + 1;
        kol.pop_back();
    }
    kol.push_back({x, ile});
}

void zdejmij(){
    if (kol.front().second == 0){
        kol.pop_front();
    } else {
        kol.front().second = kol.front().second - 1;
    }
}

int MAX(){
    if (kol.empty()){
        return (-1000000009);
    }
    return kol.front().first;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    for (int i = 0; i < n; i++){
        int a, b;
        cin >> a >> b;
        l.push_back({a, b});
    }

    int max_wyn = 1;
    int glowa = 1;
    int ogon = 1;
    while (ogon <= n){
        while (glowa <= n && MAX() <= l[glowa].second){
            wstaw(l[glowa].first);
            glowa++;
        }
        max_wyn = max(max_wyn, glowa - ogon);
        zdejmij();
        ogon++;
    }
    cout << max_wyn << endl;

    return 0;
}
