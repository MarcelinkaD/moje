/**
 * @file:      fastio.h, Mistrz Programowania 2025
 * @author:    Szymon Hajderek
 *
 * @desc:      Biblioteczka do szybkiego wczytywania danych.
 *             Identyczny plik znajduje się w systemie sprawdzającym.
 *             Dostępne funkcje:
 *
 *               wczytaj_nm(int& n, int& m):
 *                     wczytuje z wejścia n oraz m i zapisuje je do podanych zmiennych
 *
 *               void wczytaj_zapytanie(char& typ, int& arg1, int& arg2):
 *                     wczytuje z wejścia n oraz m i zapisuje je do podanych zmiennych
 *                
 *               void wypisz(int kolejny_wynik):
 *                     wypisuje liczbę na standardowe wyjście
 */

#include <iostream>
using namespace std;

inline void wczytaj_nm(int& n, int& m);
inline void wczytaj_zapytanie(char& typ, int& arg1, int& arg2);
inline void wypisz(int kolejny_wynik);

namespace fastio {

inline int rint() {
  static int res; static int c; res = 0;
  do { c = getchar_unlocked(); } while(!isdigit(c));
  while(isdigit(c)) { res = res * 10 + (c - '0'), c = getchar_unlocked(); }
  return res;
}

inline void pint(int val) {
  static char buff[100]; static int ptr = 0;
  do { buff[ptr++] = char(val % 10); val /= 10; } while(val);
  while(ptr) { putchar_unlocked('0' + buff[--ptr]); }
  putchar_unlocked('\n');
}

}

inline void wczytaj_nm(int& n, int& m) {
  n = fastio::rint(), m = fastio::rint();
};

inline void wczytaj_zapytanie(char& typ, int& arg1, int& arg2) {
  typ = char(getchar_unlocked()), arg1 = fastio::rint();
  if(typ != 'C') arg2 = fastio::rint();
  else arg2 = 0;
}

inline void wypisz(int kolejny_wynik) {
  fastio::pint(kolejny_wynik);
}