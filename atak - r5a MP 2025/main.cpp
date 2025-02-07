//https://szkopul.edu.pl/c/mistrz-programowania-2025/p/r5a/
#include <bits/stdc++.h>
using namespace std;

bool inRange(int x, int y) {
    return ((x <= 8 && y <= 8) && (x > 0 && y > 0));
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    unordered_map<char, int> co = {{'a', 1}, {'b', 2}, {'c', 3}, {'d', 4},
                        {'e', 5}, {'f', 6}, {'g', 7}, {'h', 8}};
    pair<int, int> ruchy[8] = {{-1, 2}, {1, 2}, {2, 1}, {-2, 1}, {1, -2}, {-1, -2}, {-2, -1}, {2, -1}};

    char s;
    int y;
    cin >> s >> y;
    int x = co[s];
    int w = 0;

    for (int i = 0; i < 8; i++){
        int nx, ny;
        nx = x + ruchy[i].first;
        ny = y + ruchy[i].second;
        if (inRange(nx, ny)) w++;
    }
    cout << w << endl;

    return 0;
}
