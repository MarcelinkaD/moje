//https://szkopul.edu.pl/c/map-2024_2025/p/bit/
#include <bits/stdc++.h>
using namespace std;

unordered_map<int, int> zlicz;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;

    if (n == 1){
        cout << "TAK" << endl;
        return 0;
    }

    for (int i = 0; i < n; i++){
        int x;
        cin >> x;
        zlicz[x]++;
    }

    if (n % 2 == 1) {
        bool czy_mam_sr = 0;
        for (pair<int, int> para : zlicz) {
            if (para.second % 2 == 1) {
                if (!czy_mam_sr) {
                    czy_mam_sr = 1;
                } else {
                    cout << "NIE" << endl;
                    return 0;
                }
            }
        }
        if (czy_mam_sr) {
            cout << "TAK" << endl;
        } else {
            cout << "NIE" << endl;
        }
    } else {
        for (pair<int, int> para : zlicz) {
            if (para.second % 2 == 1) {
                cout << "NIE" << endl;
                return 0;
            }
        }
        cout << "TAK" << endl;
    }

    return 0;
}
