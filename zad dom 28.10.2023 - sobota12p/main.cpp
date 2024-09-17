// 1) https://szkopul.edu.pl/problemset/problem/JVczx9SUMEmDCu0Y552_Zryh/site/?key=statement
/*
#include <iostream>
using namespace std;

const int MAXN = 200004;
int l[MAXN];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> l[i];
    }

    int ogon = 0;
    int glowa = 1;
    int w = 1;
    int max_pom = -1;

    while (ogon < n - 1) {
        while (glowa < n - 1) {
            max_pom = max(max_pom, l[glowa]);
            glowa++;
            if (glowa != n && max_pom < min(l[ogon], l[glowa])) {
                w++;
            }
            if (l[glowa] > l[ogon]) {
                break;
            }
        }
        ogon++;
        glowa = ogon + 1;
        max_pom = -1;
        if (glowa != n && max_pom < min(l[ogon], l[glowa])) {
            w++;
        }
    }

    cout << w << endl;

    return 0;
}
*/

// 2) https://szkopul.edu.pl/problemset/problem/uIyU0DBwEdBOI2YO4tKPtZ1V/site/?key=statement
#include <iostream>
using namespace std;

const int MAXN = 200004;
int gdzie_i[MAXN];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int n, w;
    w = 1;
    cin >> n;

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        gdzie_i[x] = i;
    }

    int pocz = gdzie_i[1];
    int kon = gdzie_i[1];

    for (int i = 2; i <= n; i++) {
        pocz = min(pocz, gdzie_i[i]);
        kon = max(kon, gdzie_i[i]);

        if (kon - pocz + 1 == i) {
            w++;
        }
    }
    cout << w << endl;
    return 0;
}

