#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
#define int long long

struct drzewo {
    vector<pair<int, int>> tree;
    int M;
    drzewo(int M): M(M) {
        tree = vector<pair<int, int>>(2 * M + 4, {0, 0});
    }
    
    void update(int v, int x) {
        int orig = v;
        v += M;
        tree.at(v).first = x;
        tree.at(v).second = orig;
        v /= 2;
        while (v > 1) {
            if (tree.at(2 * v) > tree.at(2 * v + 1)) {
                tree.at(v).first = tree.at(2 * v).first;
                tree.at(v).second = tree.at(2 * v).second;
            } else {
                tree.at(v).first = tree.at(2 * v + 1).first;
                tree.at(v).second = tree.at(2 * v + 1).second;

            }
            v /= 2;
        }
    }
    
    pair<int, int> qery(int l, int r) const {
        int max_ = 0;
        int idx = 0;
        int origl = l;
        int origr = r;
        l += M;
        r += M;
        max_ = tree.at(l).first;
        idx = tree.at(l).second;
        if (tree.at(r).first > max_ || tree.at(r).second == origr) {
            max_ = tree.at(r).first;
            idx = tree.at(r).second;
        }
        
        while (l/2 != r/2) {
            if (l % 2 == 0)
                if (tree.at(l + 1).first > max_ || tree.at(l + 1).second == origl || tree.at(l + 1).second == origr) {
                    max_ = tree.at(l + 1).first;
                    idx = tree.at(l + 1).second;
                }
            if (r % 2 == 1)
                if (tree.at(r - 1).first > max_ || tree.at(r - 1).second == origl || tree.at(r - 1).second == origr) {
                    max_ = tree.at(r - 1).first;
                    idx = tree.at(r - 1).second;
                }
            r /= 2;
            l /= 2;
        }
        return {max_, idx};
    }
};

int solve(int l, int r, int n,  const drzewo &tree) {
    if (l >= r) {
        return 1;
    }
    int idx = tree.qery(l, r).second;
    int l2 = 0;
    int r2 = 0;
    if (idx - 1 >= l) 
        l2 = solve(l, idx - 1, n,  tree);

    if (idx + 1 <= r)
        r2 = solve(idx + 1, r, n, tree);
    return min(l2, r2) + 1;
}


signed main() {
    int n; cin >> n;
    int m = 1;
    while (m < n)
        m *= 2;
    drzewo tree(m);
    for (int i = 0; i < n; i++) {
        int a; cin >> a;
        tree.update(i, a);
    }
    cout << solve(0, n- 1, n, tree);
    return 0;
}