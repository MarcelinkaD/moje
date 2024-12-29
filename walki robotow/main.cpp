//Linki z wiedza:
// Mergesort: https://www.geeksforgeeks.org/cpp-program-for-merge-sort/
// Silne Skladowe: https://eduinf.waw.pl/inf/alg/001_search/0129.php  https://favtutor.com/blogs/strongly-connected-components
// Dfs ze Stosem: https://www.geeksforgeeks.org/iterative-depth-first-traversal/
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 200005;
vector<unordered_set<int>> graf(MAXN), grafTra(MAXN), graf_sss(MAXN);
vector<vector<int>> sss;
stack<int> stos_koncow;
bool czy_odw[MAXN];
int sss_id[MAXN];
int n;

struct robot {
    int s;
    int z;
    int ind;
};

void dfs(int od) {
    stack<int> stos;
    stos.push(od);
    czy_odw[od] = 1;

    while (!stos.empty()) {
        int u = stos.top();
        bool czy_odw_sasiad = 0;

        for (auto sasiad : graf[u]) {
            if (!czy_odw[sasiad]) {
                czy_odw[sasiad] = 1;
                stos.push(sasiad);
                czy_odw_sasiad = 1;
                break;
            }
        }

        if (!czy_odw_sasiad) {
            stos.pop();
            stos_koncow.push(u);
        }
    }
}

void dfsTra(int od, vector<int>& spojna_sil_skl) {
    stack<int> stos;
    stos.push(od);
    czy_odw[od] = 1;

    while (!stos.empty()) {
        int u = stos.top();
        stos.pop();
        spojna_sil_skl.push_back(u);

        for (auto sasiad : grafTra[u]) {
            if (!czy_odw[sasiad]) {
                czy_odw[sasiad] = 1;
                stos.push(sasiad);
            }
        }
    }
}

void znajdz_sss() {
    for (int i = 0; i < n; i++) {
        if (!czy_odw[i]) {
            dfs(i);
        }
    }

    fill(czy_odw, czy_odw + n, 0);
    while (!stos_koncow.empty()) {
        int u = stos_koncow.top();
        stos_koncow.pop();
        if (!czy_odw[u]) {
            vector<int> spojna_sil_skl;
            dfsTra(u, spojna_sil_skl);
            sss.push_back(spojna_sil_skl);
            for (auto v : spojna_sil_skl) {
                sss_id[v] = sss.size() - 1;
            }
        }
    }
}

vector<int> oblicz_wchodzace_krawedzie() {
    vector<int> wchadzace_krawedzie(sss.size(), 0);

    for (int u = 0; u < n; u++) {
        for (auto v : graf[u]) {
            if (sss_id[u] != sss_id[v]) {
                graf_sss[sss_id[v]].insert(sss_id[u]);
            }
        }
    }

    for (int i = 0; i < sss.size(); i++) {
        wchadzace_krawedzie[i] = graf_sss[i].size();
    }

    return wchadzace_krawedzie;
}


long long polacz(vector<int>& tab, vector<int>& temp, int lewo, int srodek, int prawo) {
    int i = lewo, j = srodek + 1, k = lewo;
    long long ile_inw = 0;
    while (i <= srodek && j <= prawo) {
        if (tab[i] <= tab[j]) {
            temp[k] = tab[i];
            k++;
            i++;
        } else {
            temp[k] = tab[j];
            k++;
            j++;
            ile_inw += (srodek + 1 - i);
        }
    }
    while (i <= srodek) {
        temp[k] = tab[i];
        k++;
        i++;
    }

    while (j <= prawo) {
        temp[k++] = tab[j++];
        k++;
        j++;
    }

    for (i = lewo; i <= prawo; i++) {
        tab[i] = temp[i];
    }

    return ile_inw;
}

long long mergeSort(vector<int>& tab, vector<int>& temp, int lewo, int prawo) {
    if (lewo >= prawo) {
        return 0;
    }
    int srodek = lewo + (prawo - lewo) / 2;
    long long ile_inw = 0;
    ile_inw += mergeSort(tab, temp, lewo, srodek);
    ile_inw += mergeSort(tab, temp, srodek + 1, prawo);
    ile_inw += polacz(tab, temp, lewo, srodek, prawo);
    return ile_inw;
}

long long licz_inwersje(vector<int>& tab) {
    if (tab.size() < 2) {
        return 0;
    }
    vector<int> temp(tab.size());
    return mergeSort(tab, temp, 0, tab.size() - 1);
}

long long licz_krawedzie_naj_silniejszej(int ind_naj_sil, const vector<robot>& roboty) {
    const vector<int>& spojna_sil_skl = sss[ind_naj_sil];
    vector<robot> silnie_roboty;
    for (auto ind : spojna_sil_skl) {
        silnie_roboty.push_back(roboty[ind]);
    }

    sort(silnie_roboty.begin(), silnie_roboty.end(), [](const robot& a, const robot& b) {
        return a.s < b.s;
    });

    vector<int> porzadek_zwin;
    for (const auto& rob : silnie_roboty) {
        porzadek_zwin.push_back(rob.z);
    }

    long long ile_inw = licz_inwersje(porzadek_zwin);
    long long calkowita_para = static_cast<long long>(spojna_sil_skl.size()) * (spojna_sil_skl.size() - 1) / 2;
    long long wspolne_krawedzie = calkowita_para - ile_inw;
    long long liczba_krawedzi = 2 * calkowita_para - wspolne_krawedzie;

    return liczba_krawedzi;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n;

    vector<robot> roboty(n);
    for (int i = 0; i < n; i++) {
        robot rob_top;
        cin >> rob_top.s;
        cin >> rob_top.z;
        rob_top.ind = i;
        roboty[i] = rob_top;
    }

    vector<robot> sort_sil = roboty;
    sort(sort_sil.begin(), sort_sil.end(), [](robot &a, robot &b) {
        return a.s < b.s;
    });

    for (int i = 0; i < n - 1; i++) {
        int ind_sil = sort_sil[i + 1].ind;
        int ind_slab = sort_sil[i].ind;
        graf[ind_sil].insert(ind_slab);
        grafTra[ind_slab].insert(ind_sil);
    }

    vector<robot> sort_zwin = roboty;
    sort(sort_zwin.begin(), sort_zwin.end(), [](robot &a, robot &b) {
        return a.z < b.z;
    });

    for (int i = 0; i < n - 1; i++) {
        int ind_zwin = sort_zwin[i + 1].ind;
        int ind_mniej_zwin = sort_zwin[i].ind;
        graf[ind_zwin].insert(ind_mniej_zwin);
        grafTra[ind_mniej_zwin].insert(ind_zwin);
    }


    znajdz_sss();
    vector<int> wchadzace_krawedzie = oblicz_wchodzace_krawedzie();
    int licz_bez_wcho = 0;
    int ind_bez_wcho = -1;

    for (int i = 0; i < wchadzace_krawedzie.size(); i++) {
        if (wchadzace_krawedzie[i] == 0) {
            licz_bez_wcho++;
            ind_bez_wcho = i;
            if (licz_bez_wcho > 1) {
                cout << "NIE";
                return 0;
            }
        }
    }
    long long licz_kra_naj = licz_krawedzie_naj_silniejszej(ind_bez_wcho, roboty);
    long long max_kra = static_cast<long long>(sss[ind_bez_wcho].size()) * (sss[ind_bez_wcho].size() - 1);

    if (sss[ind_bez_wcho].size() % 2 == 1 && licz_kra_naj < max_kra) {
        cout << "TAK";
        return 0;
    }

    if (sss[ind_bez_wcho].size() % 2 == 0) {
        cout << "TAK";
    } else {
        cout << "NIE";
    }

    return 0;
}

