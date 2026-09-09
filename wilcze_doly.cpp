#include <bits/stdc++.h>
using namespace std;

deque<pair<int,int>> kol_max;

void dodaj(int war, int ind){
    while(!kol_max.empty() && kol_max.back().first <= war) kol_max.pop_back();
    kol_max.push_back({war, ind});
}

void usun_stare(int kon, int d){
    while(!kol_max.empty() && kol_max.front().second < kon + d - 1) kol_max.pop_front();
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, p, d;
    cin >> n >> p >> d;

    vector<int> maxima(n+1, 0);
    vector<long long> sumy(n+1, 0);
    vector<int> liczby(1, 0);
    for(int i=0;i<n;i++){
        int x; cin >> x;
        liczby.push_back(x);
    }

    for(int i=1;i<=n;i++) sumy[i] = sumy[i-1] + liczby[i];
    for(int i=d;i<=n;i++)  maxima[i] = (int)(sumy[i] - sumy[i-d]);

    int pocz = d - 1;         
    int kon  = 1;             
    int akt_prze = d - 1;     
    long long akt_suma = sumy[d-1];
    int max_wyn = -1;
    dodaj(maxima[pocz], pocz);

    while(kon <= n){
        if(kol_max.empty()) dodaj(maxima[pocz], pocz);
        while(pocz < n && !kol_max.empty()
              && (akt_suma + liczby[pocz+1]) - kol_max.front().first <= p){
            ++pocz;
            ++akt_prze;
            akt_suma += liczby[pocz];
            max_wyn = max(max_wyn, akt_prze);
            dodaj(maxima[pocz], pocz);
        }
        akt_suma -= liczby[kon];
        usun_stare(kon + 1, d);
        ++kon;
        --akt_prze;
        max_wyn = max(max_wyn, akt_prze);
    }

    cout << max_wyn << '\n';
    return 0;
}
