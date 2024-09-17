// 1) Bajtocka flaga (str. 42)
#include <iostream>
#include <map>
#include <vector>
using namespace std;

int main()
{
    int n, w;
    cin >> n;
    vector<int> l;
    map<int, int> parz;
    map<int, int> nie_parz;
    pair<pair<int, int>, pair<int, int>> parz_max;
    parz_max.first.second = -1;
    pair<pair<int, int>, pair<int, int>> nie_parz_max;
    nie_parz_max.first.second = -1;
    w = 0;

    for (int i = 1; i <= n; i++) {
        int x;
        cin >> x;
        l.push_back(x);

        if (i % 2 == 0) {
            parz[x]++;

            if (parz_max.first.second < parz[x]) {
                parz_max.first.second = parz[x];
                parz_max.first.first = x;
            }

        } else {
            nie_parz[x]++;

            if (nie_parz_max.first.second < nie_parz[x]) {
                nie_parz_max.first.second = nie_parz[x];
                nie_parz_max.first.first = x;
            }

        }
    }

    for (int i = 0; i < n; i++) {
        if (i % 2 != 0) {
            if (l[i] != parz_max.first.second && parz_max.second.second < parz[l[i]]) {
                parz_max.second.second = parz[l[i]];
                parz_max.second.first = l[i];
            }

        } else {
            if (l[i] != nie_parz_max.first.second && nie_parz_max.second.second < nie_parz[l[i]]) {
                nie_parz_max.second.second = nie_parz[l[i]];
                nie_parz_max.second.first = l[i];
            }
        }
    }

    int lidp, lidn, licz_nie_parz, licz_parz;

    if (n % 2 == 0) {
        licz_parz = n / 2;
        licz_nie_parz = n / 2;
    } else {
        licz_nie_parz = n / 2 + 1;
        licz_parz = n / 2;
    }

    lidp = parz_max.first.first;
    lidn = nie_parz_max.first.first;

    if (lidp != lidn) {
        w += licz_parz - parz_max.first.second;
        w += licz_nie_parz - nie_parz_max.first.second;
    } else {
        int w2 = 0;
        w += licz_parz - parz_max.first.second;
        w += licz_nie_parz - nie_parz_max.second.second;
        w2 += licz_parz - parz_max.second.second;
        w2 += licz_nie_parz - nie_parz_max.first.second;
        w = max(w2, w);
    }

    cout << w << endl;

    return 0;
}
