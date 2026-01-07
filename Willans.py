import math

def willans_formula(n):
    """Calcule le n-ième nombre premier en utilisant la formule de Willans."""
    return 1 + sum([
        math.floor(pow(n / sum([
            math.floor(pow(math.cos(math.pi * (math.factorial(j - 1) + 1) / j), 2))
            for j in range(1, i + 1)
        ]), 1 / n))
        for i in range(1, pow(2, n) + 1)
    ])

def main():
    """Fonction principale pour demander à l'utilisateur de saisir un rang et afficher le nombre premier correspondant."""
    while True:
        try:
            n = int(input("Veuillez entrer le rang du nombre premier que vous souhaitez trouver (entre 1 et 20): "))
            if n < 1 or n > 20:
                print("Le rang doit être compris entre 1 et 20. Veuillez réessayer.")
            else:
                prime = willans_formula(n)
                print(f"Le {n}-ième nombre premier est {prime}")
                break
        except ValueError:
            print("Veuillez entrer un nombre entier valide (entre 1 et 20). Veuillez réessayer.")

if __name__ == "__main__":
    main()

