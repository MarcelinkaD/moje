#include <bits/stdc++.h>
using namespace std;

static const int MOD = 1000000007;

struct Stan {
    int c111, c110, c011, c101, c010;
    int xorWar;
    bool czyKolejA;
};

struct StanHasz {
    size_t operator()(const Stan &st) const {
        auto h1 = std::hash<long long>()(
            (1LL * st.c111 * 1000003) ^
            (1LL * st.c110 * 10000) ^
            (1LL * st.c011 * 9973) ^
            (1LL * st.c101 * 1009) ^
            (1LL * st.c010 * 31) ^
            (1LL * st.xorWar * 7) ^
            (st.czyKolejA ? 1234567LL : 7654321LL)
        );
        return (size_t)h1;
    }
};

struct StanEq {
    bool operator()(const Stan &a, const Stan &b) const {
        return (a.c111 == b.c111 && a.c110 == b.c110 && a.c011 == b.c011
             && a.c101 == b.c101 && a.c010 == b.c010
             && a.xorWar == b.xorWar && a.czyKolejA == b.czyKolejA);
    }
};

unordered_map<Stan, long long, StanHasz, StanEq> memo;

long long dfs(int c111, int c110, int c011, int c101, int c010, int xorWar, bool czyKolejA)
{
    Stan st{c111, c110, c011, c101, c010, xorWar, czyKolejA};
    auto it = memo.find(st);
    if (it != memo.end()) {
        return it->second;
    }

    if (c111 == 0 && c110 == 0 && c011 == 0) {
        long long w = (xorWar == 0 ? 1LL : 0LL);
        memo[st] = w;
        return w;
    }

    long long wyn = 0;
    bool czyWygrana = (xorWar != 0);

    auto dodajRuch = [&](long long liczbaSpos, int nc111, int nc110, int nc011, int nc101, int nc010, int nxorWar) {
        if (liczbaSpos == 0) return;
        long long w = dfs(nc111, nc110, nc011, nc101, nc010, nxorWar, !czyKolejA);
        wyn = (wyn + (liczbaSpos * w) % MOD) % MOD;
    };

    auto XOR = [&](int oldG, int newG) {
        return (xorWar ^ oldG ^ newG);
    };

    if (c111 > 0) {
        {
            int nowyXor = XOR(2, 1);
            long long liczbaSpos = 1LL * c111;
            if (czyWygrana) {
                if (nowyXor == 0) {
                    dodajRuch(liczbaSpos, c111 - 1, c110 + 1, c011, c101, c010, 0);
                }
            } else {
                if (nowyXor != 0) {
                    dodajRuch(liczbaSpos, c111 - 1, c110 + 1, c011, c101, c010, nowyXor);
                }
            }
        }
        {
            int nowyXor = XOR(2, 1);
            long long liczbaSpos = 1LL * c111;
            if (czyWygrana) {
                if (nowyXor == 0) {
                    dodajRuch(liczbaSpos, c111 - 1, c110, c011 + 1, c101, c010, 0);
                }
            } else {
                if (nowyXor != 0) {
                    dodajRuch(liczbaSpos, c111 - 1, c110, c011 + 1, c101, c010, nowyXor);
                }
            }
        }
        {
            int nowyXor = XOR(2, 0);
            long long liczbaSpos = 1LL * c111;
            if (czyWygrana) {
                if (nowyXor == 0) {
                    dodajRuch(liczbaSpos, c111 - 1, c110, c011, c101 + 1, c010, 0);
                }
            } else {
                if (nowyXor != 0) {
                    dodajRuch(liczbaSpos, c111 - 1, c110, c011, c101 + 1, c010, nowyXor);
                }
            }
        }
    }

    if (c110 > 0) {
        int nowyXor = XOR(1, 0);
        long long liczbaSpos = 1LL * c110;
        if (czyWygrana) {
            if (nowyXor == 0) {
                dodajRuch(liczbaSpos, c111, c110 - 1, c011, c101, c010 + 1, 0);
            }
        } else {
            if (nowyXor != 0) {
                dodajRuch(liczbaSpos, c111, c110 - 1, c011, c101, c010 + 1, nowyXor);
            }
        }
    }

    if (c011 > 0) {
        int nowyXor = XOR(1, 0);
        long long liczbaSpos = 1LL * c011;
        if (czyWygrana) {
            if (nowyXor == 0) {
                dodajRuch(liczbaSpos, c111, c110, c011 - 1, c101, c010 + 1, 0);
            }
        } else {
            if (nowyXor != 0) {
                dodajRuch(liczbaSpos, c111, c110, c011 - 1, c101, c010 + 1, nowyXor);
            }
        }
    }

    memo[st] = wyn;
    return wyn;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;

    auto Grundy = [&](int a, int b, int c){
        int maska = (a << 2) | (b << 1) | (c);
        switch(maska){
            case 2: return 0;
            case 5: return 0;
            case 3: return 1;
            case 6: return 1;
            case 7: return 2;
        }
        return -1;
    };

    int c111 = 0, c110 =0, c011 = 0, c101 = 0, c010 = 0;
    int x = 0;

    for (int i = 1; i <= n; i++){
        int a, b, c;
        cin >> a >> b >> c;
        if (i == 1) {
            continue;
        }
        int g = Grundy(a, b, c);
        if (g == 0) {
            int maska = (a << 2)|(b << 1)|c;
            if (maska == 2) { c010++; }
            else { c101++; }
        } else if (g == 1) {
            int maska = (a << 2)|(b << 1)|c;
            if (maska == 3) { c011++; }
            else { c110++; }
        } else {
            c111++;
        }
        x ^= g;
    }

    if (x != 0) {
        cout << 'A'<< endl;
    } else {
        cout << 'B' << endl;
    }

    long long wynik = dfs(c111, c110, c011, c101, c010, x, true);
    wynik %= MOD;
    cout << wynik << endl;

    return 0;
}
