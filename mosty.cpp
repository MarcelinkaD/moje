#include <bits/stdc++.h>
#include "moslib.h"
using namespace std;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n = daj_n();
    vector<long long> odl_od_jed(n + 1, 0);

    for (int i = 2; i <= n; i++){
        odl_od_jed[i] = odleglosc(1, i);
    }

    vector<int> wierz(n - 1);
    iota(wierz.begin(), wierz.end(), 2);
    sort(wierz.begin(), wierz.end(), [&](int a, int b) {
        return odl_od_jed[a] < odl_od_jed[b];
    });

    vector<pair<int, int>> kraw_wyn;
    vector<long long> odl_wyn;

    vector<int> pop_wie;
    pop_wie.reserve(n);
    pop_wie.push_back(1);

    for (int akt_wie : wierz){
        for (int i = (int)pop_wie.size() - 1; i >= 0; i--){
            int now_wie = pop_wie[i];
            long long trzeba = odl_od_jed[akt_wie] - odl_od_jed[now_wie];
            if (trzeba <= 0) continue;
            long long droga = odleglosc(akt_wie, now_wie);
            if (droga == trzeba){
                kraw_wyn.push_back({now_wie, akt_wie});
                odl_wyn.push_back(droga);
                break;
            }
        }
        pop_wie.push_back(akt_wie);
    }

    odpowiedz(kraw_wyn, odl_wyn);
    return 0;
}
