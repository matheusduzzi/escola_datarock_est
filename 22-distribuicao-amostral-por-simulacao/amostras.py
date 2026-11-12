"""As funções da aula «Distribuição amostral por simulação», para usar no exercício.

from amostras import sortear, repetir
"""
import statistics


def sortear(rng, valores, k):
    return [valores[int(rng.random() * len(valores))] for _ in range(k)]


def repetir(rng, valores, n, repeticoes=10000):
    medias, desvios = [], []
    for _ in range(repeticoes):
        amostra = sortear(rng, valores, n)
        medias.append(statistics.mean(amostra))
        desvios.append(statistics.stdev(amostra))
    return medias, desvios
