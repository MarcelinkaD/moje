#include <bits/stdc++.h>
#include <fstream>
typedef long long ll;
using namespace std;

vector<ll> pop_war;
ll bin_na_dzies(string s){
    ll czy_min = 1;
    if (s[0] == '-'){
        czy_min = -1;
        s = s.substr(1, s.size() - 1);
    }
    ll wyn = 0;
    ll akt_pot = 1;
    for (int i = s.size() - 1; i >= 0; i--){
        wyn += (ll)(s[i] - '0') * akt_pot;
        akt_pot *= 2;
    }
    return wyn * czy_min;
}

string dzies_na_bin(ll x){
    string w;
    if (x == 0){
        w = "0";
    }
    bool czy_min = false;
    if (x < 0){
        x *= -1;
        czy_min = true;
    }
    while (x > 0){
        w = (char)(x % 2 + 48) + w;
        x /= 2;
    }
    if (czy_min){
        w = '-' + w;
    }
    return w;
}

string czwor_na_bin(string s){
    string wyn;
    if (s[0] == '-'){
        wyn += '-';
        s = s.substr(1, s.size() - 1);
    }
    for (auto znak : s){
        string kaw = dzies_na_bin(znak - 48);
        while (kaw.size() % 2 != 0){
            kaw = '0' + kaw;
        }
        wyn += kaw;
    }
    return wyn;
}

string osem_na_bin(string s){
    string wyn;
    if (s[0] == '-'){
        wyn += '-';
        s = s.substr(1, s.size() - 1);
    }
    for (auto znak : s){
        string kaw = dzies_na_bin(znak - 48);
        while (kaw.size() % 3 != 0){
            kaw = '0' + kaw;
        }
        wyn += kaw;
    }
    return wyn;
}

ll oblicz(ll t2, ll j){
    ll max_wyn = -1;
    for (int i = 1; i <= pop_war.size(); i++){
        ll t1 = pop_war[i - 1];
        ll r = (t1 - t2) * (t1 - t2);
        ll temp = j - i;
        max_wyn = max(max_wyn, (r + temp - 1) / temp);
    }
    return max_wyn;
}

int main(){
    fstream wej1, wej2, wej3, wyj;

    wej1.open("dane_systemy1.txt", ios::in);
    wej2.open("dane_systemy2.txt", ios::in);
    wej3.open("dane_systemy3.txt", ios::in);
    wyj.open("wyniki_systemy.txt", ios::out);

    ll min1 = LLONG_MAX;
    ll min2 = LLONG_MAX;
    ll min3 = LLONG_MAX;
    ll max1 = LLONG_MIN;
    ll max2 = LLONG_MIN;
    ll max3 = LLONG_MIN;
    ll akt_czas = 12;
    int wyn2 = 0;
    int wyn3 = 0;
    ll skok = -1;
    ll l = 1;
    while (!wej1.eof() && !wej2.eof() && !wej3.eof()){
        string g1, g2, g3;
        string s1, s2, s3;
        wej1 >> g1 >> s1;
        wej2 >> g2 >> s2;
        wej3 >> g3 >> s3;

        ll temp1 = bin_na_dzies(s1);
        ll temp2 = bin_na_dzies(czwor_na_bin(s2));
        ll temp3 = bin_na_dzies(osem_na_bin(s3));
        min1 = min(min1, temp1);
        min2 = min(min2, temp2);
        min3 = min(min3, temp3);
        if (akt_czas != bin_na_dzies(g1) && akt_czas != bin_na_dzies(czwor_na_bin(g2)) && akt_czas != bin_na_dzies(osem_na_bin(g3))){
            wyn2++;
        }
        akt_czas += 24;

        if (max1 < temp1){
            wyn3++;
        } else if (max2 < temp2){
            wyn3++;
        } else if (max3 < temp3){
            wyn3++;
        }
        max1 = max(max1, temp1);
        max2 = max(max2, temp2);
        max3 = max(max3, temp3);

        skok = max(skok, oblicz(temp1, l));

        l++;
        pop_war.push_back(temp1);
    }

    

    wyj << "ZAD 1. Stacja 1: " << dzies_na_bin(min1) << " Stacja 2: " << dzies_na_bin(min2) << " Stacja 3: " << dzies_na_bin(min3) << '\n';
    wyj << "ZAD 2. " << wyn2 << '\n';
    wyj << "ZAD 3. " << wyn3 << '\n';
    wyj << "ZAD 4. " << skok << '\n';
    wej1.close();
    wej2.close();
    wej3.close();
    wyj.close();

    return 0;
}