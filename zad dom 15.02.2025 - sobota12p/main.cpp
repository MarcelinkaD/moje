//https://szkopul.edu.pl/c/programowanie-od-podstaw/problemset/problem/Rf4E0AVIQ6vprRVEvdvj17dp/site/?key=statement
#include <bits/stdc++.h>
using namespace std;

const int MOD = 1000000007;
vector<long long> l;
unordered_map<long long, long long> dp;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    l.resize(n);

    for (int i = 0; i < n; i++){
        cin >> l[i];
    }

    long long liczba_masek = 1 << n;
    dp[0] = 1;
    for (long long maska = 1; maska < liczba_masek; maska++){
        dp[maska] = 0;
        long long suma = 0;
        long long ile = 0;
        for (int i = 0; i < n; i++){
            if ((maska >> i) & 1){
                suma += l[i];
                ile++;
            }
        }
        if (suma < 0){
            dp[maska] = 0;
            continue;
        }

        if (ile == 1){
            dp[maska] = 1;
        } else if (ile == 2){
            long long a = 0, b = 0;
            bool czy_pie = true;
            for (int i = 0; i < n; i++){
                if ((maska >> i) & 1){
                    if (czy_pie) {
                        a = l[i];
                        czy_pie = false;
                    } else {
                        b = l[i];
                    }
                }
            }
            if (a >= 0 && b >= 0) {
                dp[maska] = 2;
            } else {
                dp[maska] = 1;
            }
        } else {
            long long wyn = 0;
            for (long long i = 0; i < n; i++){
                if ((maska >> i) & 1) {
                    long long pop_maska = maska ^ (1 << i);
                    wyn = (wyn + dp[pop_maska]) % MOD;
                }
            }
            dp[maska] = wyn;
        }
    }

    cout << dp[liczba_masek - 1] % MOD << "\n";
    return 0;
}
