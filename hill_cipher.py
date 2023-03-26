import numpy as np
from sympy import Matrix
import math

def is_coprime(n, m):
    """
    Verilen iki sayının birbirleriyle aralarında asal olup olmadığını kontrol eden fonksiyon.
    """
    while m != 0:
        n, m = m, n % m
    return n == 1


def get_inverse(matrix, alphabet_len):
    """
    Verilen matrisin modüler tersini bulur.
    """
    if math.gcd(int(round(np.linalg.det(matrix))), alphabet_len) == 1:
        matrix = Matrix(matrix)
        return np.matrix(matrix.inv_mod(alphabet_len))
    else:
        return None


def find_key(group, results):
    """
    Verilen 3x3 matrisin determinantını hesaplar ve ardından determinantın 26 ile aralarında asal olup olmadığını
    kontrol edip duruma göre anahtar matrisi bulur.
    """

    det = int(np.linalg.det(group))
    if is_coprime(det, 26):

        print(f"Matris: \n{group}\nDeterminant: {det}\n26 ile aralarında asal!\n")
        inv = get_inverse(group, 26)
        print(f"Inverse of the matrix: \n{inv}\n")
        key = np.matmul(inv, results)
        print(f"Key: \n{key % 26}\n")


matrices = [[10, 17, 8], [15, 19, 14], [3, 4, 17]]

results = [[23, 24, 7], [7, 13, 16], [11, 23, 1]]

find_key(matrices, results)
