#include <iostream>
using namespace std;

const int MAXN = 1e6 + 4;
int pierw_wyst[MAXN] = {-1};
int ost_wyst[MAXN] = {-1};

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int n;
    cin >> n;
    int max_wyn = -1;
    int min_wyn = MAXN;

    for (int i = 0; i < n; i++){
        int k;
        cin >> k;

        if (pierw_wyst[k] == -1) {
            pierw_wyst[k] = i;
        } else {
            max_wyn = max(max_wyn, i - pierw_wyst[k]);
            min_wyn = min(min_wyn, i - ost_wyst[k]);
        }
        ost_wyst[k] = i;
    }

    cout << min_wyn << ' ' << max_wyn << endl;

    return 0;
}
