"""Contas da aula «Distribuições t e qui-quadrado» e os limites das tabelas do NIST.

Use no Python aberto nessa pasta:

    from estatisticas import *

Isso traz as três funções e os quatro dicionários de limites: T_DUAS_PONTAS, QUI2_5_ACIMA,
QUI2_2_5_ACIMA e QUI2_2_5_ABAIXO.

As três funções são as mesmas das seções 4, 6 e 7 da aula. Os limites vêm das tabelas
«Critical Values of the Student's t Distribution» e «Critical Values of the Chi-Square
Distribution» do NIST/SEMATECH e-Handbook of Statistical Methods (seções 1.3.6.7.2 e 1.3.6.7.4).
"""
from math import sqrt
from statistics import mean, stdev


def media_padronizada(valores, media_ref):
    return (mean(valores) - media_ref) / (stdev(valores) / sqrt(len(valores)))


def soma_de_quadrados(valores, desvio_ref):
    m = mean(valores)
    return sum((v - m) ** 2 for v in valores) / desvio_ref ** 2


def qui_quadrado_tabela(tabela):
    linhas = [sum(linha) for linha in tabela]
    colunas = [sum(coluna) for coluna in zip(*tabela)]
    total = sum(linhas)
    x2 = 0
    for i, linha in enumerate(tabela):
        for j, contado in enumerate(linha):
            esperado = linhas[i] * colunas[j] / total
            x2 += (contado - esperado) ** 2 / esperado
    graus = (len(linhas) - 1) * (len(colunas) - 1)
    return round(x2, 2), graus


# Em cada dicionário, a chave é o número de graus de liberdade, e o valor é o ponto da régua.

# t: deixa 2,5% acima (e, pela simetria, 2,5% abaixo do negativo). Coluna 0.975 do NIST.
T_DUAS_PONTAS = {
    1: 12.706,
    2: 4.303,
    3: 3.182,
    4: 2.776,
    5: 2.571,
    6: 2.447,
    7: 2.365,
    8: 2.306,
    9: 2.262,
    10: 2.228,
    11: 2.201,
    12: 2.179,
    15: 2.131,
    24: 2.064,
    29: 2.045,
    30: 2.042,
    100: 1.984,
    'sem fim': 1.96,
}

# qui-quadrado: deixa 5% acima. Coluna 0.95 da tabela de cima do NIST.
QUI2_5_ACIMA = {
    1: 3.841,
    2: 5.991,
    3: 7.815,
    4: 9.488,
    5: 11.07,
    6: 12.592,
    7: 14.067,
    8: 15.507,
    9: 16.919,
    10: 18.307,
    11: 19.675,
    12: 21.026,
    15: 24.996,
    24: 36.415,
    29: 42.557,
    30: 43.773,
    100: 124.342,
}

# qui-quadrado: deixa 2,5% acima. Coluna 0.975 da tabela de cima do NIST.
QUI2_2_5_ACIMA = {
    1: 5.024,
    2: 7.378,
    3: 9.348,
    4: 11.143,
    5: 12.833,
    6: 14.449,
    7: 16.013,
    8: 17.535,
    9: 19.023,
    10: 20.483,
    11: 21.92,
    12: 23.337,
    15: 27.488,
    24: 39.364,
    29: 45.722,
    30: 46.979,
    100: 129.561,
}

# qui-quadrado: deixa 2,5% abaixo. Coluna 0.025 da tabela de baixo do NIST.
QUI2_2_5_ABAIXO = {
    1: 0.001,
    2: 0.051,
    3: 0.216,
    4: 0.484,
    5: 0.831,
    6: 1.237,
    7: 1.69,
    8: 2.18,
    9: 2.7,
    10: 3.247,
    11: 3.816,
    12: 4.404,
    15: 6.262,
    24: 12.401,
    29: 16.047,
    30: 16.791,
    100: 74.222,
}
