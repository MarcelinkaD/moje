//https://szkopul.edu.pl/problemset/problem/Tczhl-p0p4d8QI5QKSByWTME/site/?key=statement
#include <bits/stdc++.h>
typedef std::string str;
using namespace std;

str dodaj(str a, str b){
    str wyn = "";
    int przenies = 0;
    int i = a.size() - 1;
    int j = b.size() - 1;
    while(i >= 0|| j >= 0 || przenies > 0){
        int znak_a = 0, znak_b = 0;
        if (i >= 0) {
            znak_a = a[i] - '0';
        }
        if (j >= 0) {
            znak_b = b[j] - '0';
        }
        int sum = znak_a + znak_b + przenies;
        przenies = sum / 10;
        wyn = to_string(sum % 10) + wyn;
        if (i >= 0) {
            i--;
        }
        if (j >= 0) {
            j--;
        }
    }
    return wyn;
}

str odejmij(str a, str b) {
    str wyn = "";
    int przenies = 0;
    int i = a.size() - 1;
    int j = b.size() - 1;
    while (i >= 0 || j >= 0) {
        int znak_a = 0, znak_b = 0;
        if (i >= 0) {
            znak_a = a[i] - '0';
        }
        if (j >= 0) {
            znak_b = b[j] - '0';
        }
        znak_a -= przenies;
        if (znak_a < znak_b) {
            znak_a += 10;
            przenies = 1;
        } else {
            przenies = 0;
        }
        wyn = to_string(znak_a - znak_b) + wyn;
        if (i >= 0) {
            i--;
        }
        if (j >= 0) {
            j--;
        }
    }

    size_t start = wyn.find_first_not_of('0');
    if (start != string::npos) {
        wyn = wyn.substr(start);
    } else {
        wyn = "0";
    }
    return wyn;
}

int porownaj(str a, str b) {
    size_t start_a = a.find_first_not_of('0');
    if (start_a != string::npos) {
        a = a.substr(start_a);
    } else {
        a = "0";
    }
    size_t start_b = b.find_first_not_of('0');
    if (start_b != string::npos) {
        b = b.substr(start_b);
    } else {
        b = "0";
    }
    if (a.size() > b.size()) {
        return 1;
    }
    if (a.size() < b.size()) {
        return -1;
    }
    if (a > b) {
        return 1;
    }
    if (a < b) {
        return -1;
    }
    return 0;
}

pair<int, str> parsuj(str s) {
    int znak = 1;
    if (s[0] == '-') {
        znak = -1;
        s = s.substr(1);
    } else if (s[0] == '+') {
        s = s.substr(1);
    }
    size_t pos = s.find(',');
    int d = 0;
    if (pos != string::npos) {
        d = s.size() - pos - 1;
        s = s.substr(0, pos) + s.substr(pos + 1);
    }

    size_t start = s.find_first_not_of('0');
    if (start != string::npos) {
        s = s.substr(start);
    } else {
        s = "0";
    }

    if (s != "0") {
        s += string(100 - d, '0');
    }
    return {znak, s};
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    str dod = "0";
    str ujemne = "0";
    for (int i = 0; i < n; i++) {
        str s;
        cin >> s;
        auto [znak, inna_licz] = parsuj(s);
        if (znak == 1) {
            dod = dodaj(dod, inna_licz);
        } else {
            ujemne = dodaj(ujemne, inna_licz);
        }
    }
    str suma;
    int znak;
    int co_wieksze = porownaj(dod, ujemne);
    if (co_wieksze > 0) {
        suma = odejmij(dod, ujemne);
        znak = 1;
    } else if (co_wieksze < 0) {
        suma = odejmij(ujemne, dod);
        znak = -1;
    } else {
        suma = "0";
        znak = 1;
    }
    if (suma == "0") {
        cout << "0" << endl;
    } else {
        str znak_str = (znak == -1) ? "-" : "";
        size_t len = suma.size();
        str calk, ulamek;
        if (len <= 100) {
            ulamek = string(100 - len, '0') + suma;
            calk = "0";
        } else {
            calk = suma.substr(0, len - 100);
            ulamek = suma.substr(len - 100);
        }

        while (!ulamek.empty() && ulamek.back() == '0') {
            ulamek.pop_back();
        }

        size_t start = calk.find_first_not_of('0');
        if (start != string::npos) {
            calk = calk.substr(start);
        } else {
            calk = "0";
        }
        if (ulamek.empty()) {
            cout << znak_str << calk << endl;
        } else {
            cout << znak_str << calk << "," << ulamek << endl;
        }
    }
    return 0;
}
