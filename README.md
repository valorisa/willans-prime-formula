# Willans' Prime Formula

Implémentation de la formule de C. P. Willans (1964) pour calculer le _n_-ième nombre premier à partir de son rang _n_. Projet éducatif explorant cette formule mathématique exacte mais inefficace, à partir d'un certain rang.[1][2][3]

## Description

La formule de Willans génère le _n_-ième nombre premier via une expression fermée utilisant le théorème de Wilson, des cosinus et des puissances. Elle est définie comme :

```
p_n = 1 + Σ_{i=1}^{2^n} floor( (n / π(i))^{1/n} )
```

où `π(i)` est le nombre de premiers ≤ _i_, calculé par :

```
π(i) = Σ_{j=1}^i floor( cos²(π * ((j-1)! + 1)/j ) )
```

Cette formule est exacte pour tout _n_ ≥ 1, mais sa complexité est O(2^n · n!), rendant son usage pratique impossible pour _n_ > 15 environ (limites numériques de Python).[2][1]

## Fonctionnalités

- Calcul exact du _n_-ième premier pour petits _n_ (1 ≤ _n_ ≤ 10 recommandé).
- Implémentation pure Python avec `math`.
- Tests unitaires pour validation.
- Exemples interactifs en CLI.

## Installation

```bash
git clone https://github.com/valorisa/willans-prime-formula.git
cd willans-prime-formula
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

Aucun dépendance externe requise (stdlib seulement).

## Utilisation

```bash
python nth_prime.py 5
# Sortie : 11 (5e premier)
```

Ou via le module :

```python
from nth_prime import nth_prime
print(nth_prime(10))  # 29
```

Exemples pour _n_=1 à 10 : 2, 3, 5, 7, 11, 13, 17, 19, 23, 29.[1]

## Limitations

| Rang _n_ | Temps approx. | Faisable ? | Premier |
|----------|---------------|------------|---------|
| 1-10     | <1s           | Oui       | 2-29    |
| 11-15    | 1-60s         | Limite    | 47-?    |
| >15      | >heures/jours | Non       | Overflow|

- **Performances** : Explosion exponentielle due à `2^n` et `factorial(n)`.
- **Numérique** : `math.factorial` échoue pour _n_ > 170 environ, mais boucle interne bloque avant.
- **Usage** : Éducatif/démonstratif uniquement. Pour production, utilisez le crible d'Ératosthène ou bibliothèques comme `sympy.ntheory`.[4][2]

## Structure du projet

```
├── nth_prime.py      # Implémentation principale
├── test_nth_prime.py # Tests unitaires
├── README.md         # Ce fichier
└── requirements.txt  # Vide (stdlib)
```

## Tests

```bash
python -m pytest test_nth_prime.py -v
```

Tous les tests passent pour _n_=1 à 10.

## Contributions

Forkez, PR bienvenus pour :
- Optimisations mineures (e.g., memoïsation).
- Visualisations (temps d'exécution).
- Ports (Rust, C++ pour comparer).

Respectez [Conventional Commits](https://www.conventionalcommits.org).

## Licence

MIT License. Voir [LICENSE](LICENSE).[1]

## Références

- Willans, C. P. (1964). "On Formulae for the _n_th Prime Number". *Mathematics of Computation*.
- [MathWorld: Willans' Formula](https://mathworld.wolfram.com/WillansFormula.html)[2]
- [Wikipedia: Formula for primes](https://en.wikipedia.org/wiki/Formula_for_primes)[3]

[1](https://www.youtube.com/watch?v=j5s0h42GfvM)
[2](https://mathworld.wolfram.com/WillansFormula.html)
[3](https://en.wikipedia.org/wiki/Formula_for_primes)
[4](https://dev.to/jamesrweb/willans-formula-32g4)
[5](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/40251661/ac1c2663-7939-40a0-ac88-557f06e43348/Screenshot_2026-01-07-08-58-09-54_f9ee0578fe1cc94de7482bd41accb329.jpg)
[6](https://github.com/github/markdownlint-github/blob/main/README.md)
[7](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md)
[8](https://dev.to/jonasbn/use-markdownlint-for-your-documentation-5ln)
[9](https://github.com/DavidAnson/markdownlint)
[10](https://github.com/github/markdownlint-github)
[11](https://seankilleen.com/2020/12/adding-markdown-linting-to-my-blogs-build-process-with-github-actions-and-markdownlint/)
[12](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md)
[13](https://updownpress.github.io/markdown-lint)
[14](https://stackoverflow.com/questions/73865899/trying-to-implement-willans-formula-for-the-n-th-prime-whats-the-problem-with)
[15](https://woutercompiles.it/2025/05/19/markdownlint-a-developers-best-friend-for-cleaner-markdown/)
[16](https://ericrowland.github.io/talks/Formulas_for_primes_2018.pdf)
[17](https://docs.gitlab.com/development/documentation/testing/markdownlint/)
[18](https://github.com/saeidmokaram/nthprime)
[19](https://github.com/vitaly-t/prime-lib/blob/main/src/nth-prime-approx.ts)
[20](https://github.com/oriolval/nth-prime)
[21](https://github.com/patrobinson/nth_prime/blob/main/README.md)
