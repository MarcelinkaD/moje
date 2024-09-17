// 2) Odchudzanie (str. 49)
/*
#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int maxi, w;
    maxi = -1;
    w = -1;

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;

        if (x >= maxi) {
            maxi = x;
        } else {
            w = max(w, maxi - x);
        }
    }

    cout << w << endl;

    return 0;
}
*/

// 3) Bilet (str. 49)
#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int q;
    cin >> q;

    for (int k = 0; k < q; k++) {
        int n, od_przodu, od_tylu, max_od_przodu, max_od_tylu, w;
        od_przodu = 0;
        od_tylu = 0;
        cin >> n;
        n--;
        vector<int> l;

        for (int i = 0; i < n; i++) {
            int x;
            cin >> x;
            l.push_back(x);
            od_przodu += x;
            max_od_przodu = max(max_od_przodu, od_przodu);
        }

        for (int i = n - 1; i >= 0; i--) {
            od_tylu += l[i];
            max_od_tylu = max(max_od_tylu, od_tylu);
        }

        w = max_od_tylu + max_od_przodu;
        cout << w << endl;

    }

    return 0;
}

