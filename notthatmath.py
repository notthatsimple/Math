from poly import Poly
from matrix import Matrix

if __name__ == "__main__":
        p = Poly({2: 1, 1: 2, 0: 4})
        print(p)
        print(p.evaluate(4))
