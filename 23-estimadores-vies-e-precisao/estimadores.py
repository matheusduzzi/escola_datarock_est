"""Funções da aula «Estimadores, viés e precisão», para usar no exercício.

São as mesmas das seções 4 e 5 da aula. Só usam a biblioteca padrão do Python.
"""
import statistics


def media(amostra):
    return statistics.mean(amostra)


def mediana(amostra):
    return statistics.median(amostra)


def mistura(amostra, referencia=120, peso=10):
    return (sum(amostra) + peso * referencia) / (len(amostra) + peso)


def sortear(rng, valores, k):
    return [valores[int(rng.random() * len(valores))] for _ in range(k)]


def comparar(rng, valores, regras, n, repeticoes=10000):
    estimativas = {nome: [] for nome in regras}
    for _ in range(repeticoes):
        amostra = sortear(rng, valores, n)
        for nome, regra in regras.items():
            estimativas[nome].append(regra(amostra))
    return estimativas


def resumo(estimativas, verdade):
    vies = statistics.mean(estimativas) - verdade
    erro_padrao = statistics.pstdev(estimativas)
    reqm = statistics.mean([(e - verdade) ** 2 for e in estimativas]) ** 0.5
    return round(vies, 2), round(erro_padrao, 2), round(reqm, 2)
