//https://szkopul.edu.pl/c/mistrz-programowania-2025/p/r4e/
#include <bits/stdc++.h>
using namespace std;

#ifdef WIN32
inline int getchar_unlocked() { return _getchar_nolock(); }
#endif

#ifdef WIN32
inline int putchar_unlocked(int c) { return _putchar_nolock(c); }
#endif

inline void wczytaj_nm(int& n, int& m);
inline void wczytaj_zapytanie(char& typ, int& arg1, int& arg2);
inline void wypisz(int kolejny_wynik);

namespace fastio {

inline int rint() {
  static int res; static int c; res = 0;
  do { c = getchar_unlocked(); } while(!isdigit(c));
  while(isdigit(c)) { res = res * 10 + (c - '0'), c = getchar_unlocked(); }
  return res;
}

inline void pint(int val) {
  static char buff[100]; static int ptr = 0;
  do { buff[ptr++] = char(val % 10); val /= 10; } while(val);
  while(ptr) { putchar_unlocked('0' + buff[--ptr]); }
  putchar_unlocked('\n');
}

}

inline void wczytaj_nm(int& n, int& m) {
  n = fastio::rint(), m = fastio::rint();
};

inline void wczytaj_zapytanie(char& typ, int& arg1, int& arg2) {
  typ = char(getchar_unlocked()), arg1 = fastio::rint();
  if(typ != 'C') arg2 = fastio::rint();
  else arg2 = 0;
}

inline void wypisz(int kolejny_wynik) {
  fastio::pint(kolejny_wynik);
}

struct DSU {
    int n;
    vector<int> rodzic, rnk;

    DSU(int n) : n(n), rodzic(n + 1), rnk(n + 1,0) {
        for (int i = 1; i <= n; i++){
            rodzic[i] = i;
        }
    }

    int findr(int v){
        if (rodzic[v] == v) return v;
        return rodzic[v] = findr(rodzic[v]);
    }

    bool zlacz(int a, int b){
        a = findr(a);
        b = findr(b);
        if (a == b) return false;
        if (rnk[a] < rnk[b]) swap(a, b);
        rodzic[b] = a;
        if (rnk[a] == rnk[b]) rnk[a]++;
        return true;
    }
};

static const int MAXN = 100000;
static const int LOGN = 17;
int rodzicT[LOGN + 1][MAXN + 1];
int maxWierz[LOGN + 1][MAXN + 1];
int glebokosc[MAXN + 1];

vector<pair<int, int>> graf[MAXN + 1];

void dfs(int v, int p, int w, int d){
    rodzicT[0][v] = p;
    maxWierz[0][v] = w;
    glebokosc[v] = d;
    for (auto &nx : graf[v]){
        int kolejny = nx.first;
        int ww = nx.second;
        if (kolejny == p) continue;
        dfs(kolejny, v, ww, d + 1);
    }
}

void LCA(int n){
    for (int k = 1; k <= LOGN; k++){
        for (int v = 1; v <= n; v++){
            int p = rodzicT[k - 1][v];
            rodzicT[k][v] = rodzicT[k - 1][p];
            maxWierz[k][v] = max(maxWierz[k - 1][v], maxWierz[k - 1][p]);
        }
    }
}

int liftAndGetMaxWierz(int v, int odl){
    int ret = 0;
    for (int k = 0; k <= LOGN; k++){
        if (odl & (1 << k)){
            ret = max(ret, maxWierz[k][v]);
            v = rodzicT[k][v];
        }
    }
    return ret;
}

int getMaxWierzOnPath(int x, int y){
    if (glebokosc[x] < glebokosc[y]) swap(x, y);

    int diff = glebokosc[x] - glebokosc[y];
    int ans = liftAndGetMaxWierz(x, diff);
    x =  [=](){
        int xx = x;
        for (int k = 0; k <= LOGN; k++){
            if (diff & (1 << k)) {
                xx = rodzicT[k][xx];
            }
        }
        return xx;
    }();

    if (x == y) {
        return ans;
    }

    for (int k = LOGN; k >= 0; k--){
        if (rodzicT[k][x] != rodzicT[k][y]){
            ans = max(ans, maxWierz[k][x]);
            ans = max(ans, maxWierz[k][y]);
            x = rodzicT[k][x];
            y = rodzicT[k][y];
        }
    }
    ans = max(ans, maxWierz[0][x]);
    ans = max(ans, maxWierz[0][y]);
    return ans;
}


int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n, m;
    cin >> n >> m;

    vector<tuple<char, int, int>> ops(m + 1);

    for (int i = 1; i <= m; i++){
        char c;
        int x, y;
        cin >> c >> x >> y;
        ops[i] = {c, x, y};
    }

    DSU dsu(n);

    for (int i = 1; i <= m; i++){
        auto [typ, x, y] = ops[i];
        if (typ == 'P'){
            if (dsu.zlacz(x, y)){
                graf[x].push_back({y, i});
                graf[y].push_back({x, i});
            }
        }
    }

    for (int v = 1; v <= n; v++){
        if (rodzicT[0][v] == 0){
            dfs(v, v, 0, 0);
        }
    }

    LCA(n);

    for (int v = 1; v <= n; v++){
        dsu.findr(v);
    }

    for (int i = 1; i <= m; i++){
        auto [typ, x, y] = ops[i];
        if (typ == 'Z'){
            if (dsu.findr(x) != dsu.findr(y)){
                cout << 0 << endl;
            } else {
                int b = getMaxWierzOnPath(x,y);
                if (b > i){
                    cout << 0 << endl;
                } else {
                    cout << (i - b + 1) << endl;
                }
            }
        }
    }

    return 0;
}

