//https://szkopul.edu.pl/c/map-2024_2025/p/sta/18970/
#include <bits/stdc++.h>
using namespace std;

vector<int> kolejnosc;
int wyn[5];

bool czy_licz(int akt_znak){
    return akt_znak < 10 && -1 < akt_znak;
}

bool czy_slowo(int akt_znak){
    return (akt_znak < 91 && 64 < akt_znak) || (akt_znak < 123 && 96 < akt_znak);
}

// Zoptymalizowana funkcja bez kopiowania
bool czy_palindrom(const string& s, int pocz, int koniec) {
    while (pocz < koniec) {
        char a = s[pocz], b = s[koniec];
        if (a >= 'A' && a <= 'Z') a += 32;
        if (b >= 'A' && b <= 'Z') b += 32;
        if (a != b) return false;
        pocz++, koniec--;
    }
    return true;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(nullptr);

    int n;
    cin >> n;

    for (int i = 0; i < n; i++){
        int x;
        cin >> x;
        kolejnosc.push_back(x);
    }

    cin.ignore();

    string s;
    getline(cin, s);
    int k = s.size();

    for (int i = 0; i < k; i++){
        if (s[i] == ' '){
            wyn[0]++;
        }
    }

    for (int i = 0; i < k - 1; i++){
        int akt_znak = s[i] - 48;
        int nast_znak = s[i + 1] - 48;
        if (czy_licz(akt_znak) && !czy_licz(nast_znak)){
            wyn[1]++;
        }
    }

    if (czy_licz(s[k - 1] - 48)) {
        wyn[1]++;
    }

    bool czy_bylo_slowo = false;
    int pocz_slowo = -1;
    for (int i = 0; i < k; i++) {
        if (czy_slowo(s[i])) {
            if(pocz_slowo == -1) pocz_slowo = i;
        } else {
            if (pocz_slowo != -1) {
                wyn[2]++;
                if (czy_palindrom(s, pocz_slowo, i - 1)) {
                    wyn[4]++;
                }
                pocz_slowo = -1;
                czy_bylo_slowo = true;
            }
        }

        if (czy_bylo_slowo && s[i] == '.') {
            wyn[3]++;
            czy_bylo_slowo = false;
        }
    }

    if (pocz_slowo != -1) {
        wyn[2]++;
        if (czy_palindrom(s, pocz_slowo, k - 1)) {
            wyn[4]++;
        }
    }

    for (int i = 0; i < n; i++){
        cout << wyn[kolejnosc[i] - 1] << ' ';
    }

    return 0;
}
