"""As funções da aula «Lei dos grandes números e limite central», para usar no exercício.

São as mesmas das seções 4 e 7 da aula. Só biblioteca padrão.

    from medias import sortear, fora_da_faixa, medias_de_amostras
"""
import statistics


def fora_da_faixa(valores, centro, desvio):
    abaixo = sum(x < centro - 2 * desvio for x in valores)
    acima = sum(x > centro + 2 * desvio for x in valores)
    return abaixo, acima


def sortear(rng, valores, k):
    return [valores[int(rng.random() * len(valores))] for _ in range(k)]


def medias_de_amostras(rng, valores, n, repeticoes=10000):
    return [statistics.mean(sortear(rng, valores, n)) for _ in range(repeticoes)]
