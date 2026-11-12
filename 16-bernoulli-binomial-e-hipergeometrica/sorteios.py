"""Três sorteios da aula «Bernoulli, binomial e hipergeométrica».

Rode dentro dessa pasta:  python3 sorteios.py

Cada sorteio é repetido muitas vezes. Para cada número de devolvidos, o programa mostra
a frequência com que ele saiu e as duas contas da aula: a binomial e a hipergeométrica.
Só usa a biblioteca padrão do Python.
"""
import random
from math import comb


def binomial(k, n, p):
    return comb(n, k) * p**k * (1 - p)**(n - k)


def hiper(k, N, K, n):
    return comb(K, k) * comb(N - K, n - k) / comb(N, n)


def sortear(urna, n, repor, rng):
    """Tira n itens da urna. Sem reposição, o item que saiu sai também da lista."""
    urna = list(urna)
    saiu = []
    for _ in range(n):
        i = int(rng.random() * len(urna))
        saiu.append(urna[i])
        if not repor:
            urna.pop(i)
    return saiu


def rodar(titulo, N, K, n, repor, vezes, rng):
    urna = [1] * K + [0] * (N - K)  # 1 = pedido devolvido, 0 = não devolvido
    contagem = {}
    for _ in range(vezes):
        x = sum(sortear(urna, n, repor, rng))
        contagem[x] = contagem.get(x, 0) + 1
    print(titulo)
    print("devolvidos  sorteio  binomial  hipergeométrica")
    for k in range(min(n, 8) + 1):
        print(f"{k:>10}  {contagem.get(k, 0) / vezes:>7.3f}  {binomial(k, n, K / N):>8.3f}  {hiper(k, N, K, n):>15.3f}")
    print()


rng = random.Random(16)  # o 16 faz o sorteio sair igual toda vez
rodar("1. Os 10 pedidos do dia 1, sorteio de 4 com reposição", 10, 3, 4, True, 100_000, rng)
rodar("2. Os 10 pedidos do dia 1, sorteio de 4 sem reposição", 10, 3, 4, False, 100_000, rng)
rodar("3. Os 200 pedidos de outubro, sorteio de 20 sem reposição", 200, 30, 20, False, 20_000, rng)
