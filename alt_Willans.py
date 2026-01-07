#!/usr/bin/env python3
"""
Willans Prime Formula - Calcul du n-ième nombre premier.
Projet GitHub: https://github.com/<ton-username>/willans-prime-formula
Auteur: valorisa - Janv. 2026 (Termux/Android)
"""

import math
from functools import lru_cache
import csv
import sys

@lru_cache(maxsize=1024)
def prime_indicator(j: int) -> int:
    """Indicateur de primalité (Wilson): 1 si premier, 0 sinon."""
    if j < 2:
        return 0
    fact = math.factorial(j - 1)
    arg = math.pi * (fact + 1) / j
    return math.floor(math.cos(arg) ** 2)

def pi_up_to(i: int) -> int:
    """Fonction π(i): nombre de premiers ≤ i."""
    return sum(prime_indicator(j) for j in range(1, i + 1))

def willans_formula(n: int) -> int:
    """Formule de Willans pour le n-ième premier."""
    limit = 2 ** n
    total = 0
    for i in range(1, limit + 1):
        pi_i = pi_up_to(i)
        if pi_i > 0:
            total += math.floor((n / pi_i) ** (1 / n))
    return 1 + total

def benchmark_csv(max_n: int = 10):
    """Export résultats + temps en CSV pour analyse."""
    results = []
    for n in range(1, max_n + 1):
        import time
        start = time.time()
        prime = willans_formula(n)
        duration = time.time() - start
        results.append({'n': n, 'prime': prime, 'time_s': duration})
    with open('willans_benchmark.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['n', 'prime', 'time_s'])
        writer.writeheader()
        writer.writerows(results)
    print(f"Benchmark exporté: willans_benchmark.csv (n=1-{max_n})")

def main():
    """Interface interactive."""
    print("=== Formule de Willans (C.P. Willans, 1964) ===")
    print("Limite pratique: n≤12 (exponentiel 2^n * n!)")
    while True:
        try:
            n = int(input("\nRang n (1-20, 0=benchmark, q=quit): "))
            if n == 0:
                benchmark_csv(10)
                continue
            if n < 1 or n > 20:
                print("Erreur: 1≤n≤20.")
                continue
            prime = willans_formula(n)
            print(f"Le {n}-ième premier: {prime}")
            break
        except ValueError:
            if input().lower() == 'q':
                sys.exit(0)
            print("Entrez un entier valide ou 'q'.")

if __name__ == "__main__":
    main()

