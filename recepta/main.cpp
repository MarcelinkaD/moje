#include <iostream>
using namespace std;

const int MAXN = 200007;
long long sumy_pref[MAXN] = {0};
long long pocz_i_konce[MAXN] = {0};

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);


    int n, k, q;

    cin >> n >> k >> q;

    for (int k = 0; k < n; k++){
        int pocz, kon;
        cin >> pocz >> kon;
        pocz_i_konce[pocz] += 1;
        pocz_i_konce[kon + 1] -= 1;
    }

    for (int i = 1; i <= MAXN; i++){
        pocz_i_konce[i] = pocz_i_konce[i - 1] + pocz_i_konce[i];
    }

    for (int i = 1; i <= MAXN; i++){
        if (pocz_i_konce[i] < k) {
            sumy_pref[i] = 0;
        } else {
            sumy_pref[i] = 1;
        }
        sumy_pref[i] = sumy_pref[i - 1] + sumy_pref[i];
    }

    for (int j = 0; j < q; j++) {
        int odd, doo;
        cin >> odd >> doo;
        cout << sumy_pref[doo] - sumy_pref[odd - 1] << endl;
    }

    return 0;
}
