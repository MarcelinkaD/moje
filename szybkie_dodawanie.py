# -*- coding: utf-8 -*-
# Quiz: dodawanie (3 tryby) z limitem czasu i pomiarem czasu reakcji (Python 3.7+)
import random
import threading
import queue
import time
from decimal import Decimal, getcontext, ROUND_HALF_UP
from typing import Optional, Tuple

getcontext().rounding = ROUND_HALF_UP

# Konfiguracje trybów
MODE_CONFIG = {
    "s1": {  # liczby dziesiętne
        "time_limit": 30,
        "questions": 10,
        "desc": "liczby dziesiętne (0.10–99.99)",
    },
    "s2": {  # dwie cyfry 1–9 (bez zera)
        "time_limit": 3,
        "questions": 10,
        "desc": "dwie cyfry 1–9 (bez zera)",
    },
    "s3": {  # liczba całkowita 1–10000 + cyfra 1–9
        "time_limit": 10,   # 🔹 zmienione na 10 sekund
        "questions": 10,
        "desc": "liczba całkowita (1–10000) + cyfra (1–9)",
    },
}

def timed_input(timeout: int) -> Optional[str]:
    q = queue.Queue()
    def reader():
        try:
            s = input()
        except EOFError:
            s = ""
        q.put(s)
    t = threading.Thread(target=reader, daemon=True)
    t.start()
    try:
        return q.get(timeout=timeout)
    except queue.Empty:
        return None

def losuj_s1() -> Tuple[Decimal, Decimal, Decimal, str]:
    a_c = random.randint(10, 9999)  # 0.10–99.99
    b_c = random.randint(10, 9999)
    a = (Decimal(a_c) / Decimal(100)).quantize(Decimal("0.01"))
    b = (Decimal(b_c) / Decimal(100)).quantize(Decimal("0.01"))
    poprawna = (a + b).quantize(Decimal("0.01"))
    return a, b, poprawna, "s1"

def losuj_s2() -> Tuple[Decimal, Decimal, Decimal, str]:
    a = Decimal(random.randint(1, 9))
    b = Decimal(random.randint(1, 9))
    poprawna = a + b
    return a, b, poprawna, "s2"

def losuj_s3() -> Tuple[Decimal, Decimal, Decimal, str]:
    a = Decimal(random.randint(1, 10000))
    b = Decimal(random.randint(1, 9))
    poprawna = a + b
    return a, b, poprawna, "s3"

def parse_answer(s: Optional[str], mode: str) -> Optional[Decimal]:
    if s is None:
        return None
    s = s.strip().replace(",", ".")
    if s == "":
        return None
    try:
        d = Decimal(s)
        if mode == "s1":
            return d.quantize(Decimal("0.01"))
        else:  # s2 i s3 – wynik całkowity
            return d.quantize(Decimal("1"))
    except Exception:
        return None

def fmt_number(x: Decimal, mode: str) -> str:
    return f"{x:.2f}" if mode == "s1" else f"{int(x)}"

def main():
    print("Wpisz tryb i naciśnij Enter, aby zacząć serię 10 pytań:")
    print("  • s1 – dodawanie liczb dziesiętnych (30 s na pytanie)")
    print("  • s2 – dodawanie dwóch cyfr 1–9 (3 s na pytanie)")
    print("  • s3 – dodawanie liczby całkowitej (1–10000) i cyfry (1–9) (10 s na pytanie)")
    mode = ""
    while mode not in ("s1", "s2", "s3"):
        mode = input("> ").strip().lower()
        if mode not in ("s1", "s2", "s3"):
            print("Wpisz 's1', 's2' albo 's3'.")

    cfg = MODE_CONFIG[mode]
    time_limit = cfg["time_limit"]
    questions = cfg["questions"]

    print(f"\nStart serii ({cfg['desc']}). Masz {time_limit} s na każde pytanie.\n")

    punkty = 0

    for i in range(1, questions + 1):
        if mode == "s1":
            a, b, poprawna, _ = losuj_s1()
        elif mode == "s2":
            a, b, poprawna, _ = losuj_s2()
        else:
            a, b, poprawna, _ = losuj_s3()

        print(
            f"Pytanie {i}/{questions}: {fmt_number(a, mode)} + {fmt_number(b, mode)} = ? "
            f"(limit {time_limit}s)"
        )
        print("> ", end="", flush=True)

        start_ts = time.monotonic()
        ans_text = timed_input(time_limit)
        elapsed = time.monotonic() - start_ts

        if ans_text is None:
            print(f"\n⏰ Czas minął! (> {time_limit}s). Czas: {elapsed:.2f} s. 0 pkt.\n")
            continue

        ans = parse_answer(ans_text, mode)
        if ans is None:
            print(f"⚠️ Nieprawidłowy format odpowiedzi. Czas: {elapsed:.2f} s. 0 pkt.\n")
            continue

        expected = poprawna if mode == "s1" else poprawna.quantize(Decimal("1"))
        if ans == expected:
            punkty += 1
            print(f"✅ Dobrze! +1 pkt. Czas: {elapsed:.2f} s.\n")
        else:
            print(
                f"❌ Źle. Poprawna odpowiedź: {fmt_number(poprawna, mode)}. "
                f"Czas: {elapsed:.2f} s.\n"
            )

    print(f"Koniec serii! Twój wynik: {punkty}/{questions} pkt.")

if __name__ == "__main__":
    main()
