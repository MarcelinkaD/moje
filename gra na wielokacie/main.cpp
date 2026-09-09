#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0); cin.tie(nullptr); cout.tie(0);

    int q; cin >> q;
    vector<int> dane;
    int max_dane = -10;

    while(q--){
        int a; cin >> a;
        dane.push_back(a-3);
        max_dane = max(max_dane, a-3);
    }
    vector<int> dp(max_dane+1);

    dp[0] = 0;

    for(int i = 1; i <=max_dane;i++){
        set<int> s;

        for(int j = 0;j<i;j++){
            int l = (j - 1 >= 0 && j - 1 < i ? 1 : 0);
            int p = (j + 1 >= 0 && j + 1 < i ? 1 : 0);

            int left = j - (l ? 1 : 0);
            int strat = j + 1 + (p ? 1 : 0);
            int right = i - strat;

            if(left < 0){
                left = 0;
            }
            if(right < 0){
                right = 0;
            }

            int g1 = dp[left];
            int g2 = dp[right];

            s.insert(g1 ^ g2);
        }

        int mex = 0;

        while (s.count(mex) != 0)
                mex++;
        dp[i] = mex;
    }

    for(int i = 0;i<dane.size();i++){
        if(dane[i]+3 <= 3){
            cout << "Pierwszy\n";
            continue;
        }
        if(dp[dane[i]] == 0){
            cout << "Pierwszy\n";
        }else{
            cout << "Drugi\n";
        }
    }

    return 0;
}
