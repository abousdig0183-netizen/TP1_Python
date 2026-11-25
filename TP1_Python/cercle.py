
import math


class Cercle:
    def __init__(self, rayon: float):
        self.rayon = rayon

    @property
    def rayon(self):
        """Accès au rayon."""
        return self._rayon

    @rayon.setter
    def rayon(self, valeur: float):
        """Validation du rayon."""
        if valeur <= 0:
            raise ValueError("Le rayon doit être strictement positif.")
        self._rayon = valeur

    def aire(self) -> float:
        return math.pi * self.rayon ** 2

    def perimetre(self) -> float:
        return 2 * math.pi * self.rayon

    def __str__(self):
        return f"Cercle(rayon={self.rayon})"


# Tests
c = Cercle(5.0)

print("Aire :", c.aire())
print("Périmètre :", c.perimetre())
print(c)

try:
    c.rayon = -10
except ValueError as e:
    print(f"Erreur interceptée : {e}")
