#include "sen.h"
using namespace std;

int main()
{
    rozpocznij();
    int x = zapytanie(6);
    noweZapytanie(x);
    Dane d = coDalej();
    d.fun = true;
    rozwiazanie("|427|685|391|");
    dodaj(8, 2);
    dodaj(6, 7);
    dodaj(6, 2);
    dodaj(2, 5);
    dodaj(7, 5);
    dodaj(2, 9);
    dodaj(6, 1);
    dodaj(1, 5);
    dodaj(6, 5);
    dodaj(1, 7);
    dodaj(5, 3);
    dodaj(1, 3);
    dodaj(4, 3);
    dodaj(4, 10);
    sprawdzGraf();
    return 0;
}
