"""A tabela t no Python, só com a biblioteca padrão.

t_acumulada(x, gl) é a chance de um valor da distribuição t com gl graus de liberdade ficar
abaixo de x. t_critico(nivel, gl) é o número da tabela t para um intervalo de nivel (0.95 dá o
da coluna 0,975). Os graus de liberdade podem ter vírgula, como os da receita de Welch.
No SciPy, a mesma conta é scipy.stats.t.cdf(x, gl) e scipy.stats.t.ppf((1 + nivel) / 2, gl).
"""
import math
from functools import lru_cache


def _beta_incompleta(a, b, x):
    # Fração contínua da beta incompleta regularizada (método de Lentz).
    if x <= 0:
        return 0.0
    if x >= 1:
        return 1.0
    if x > (a + 1) / (a + b + 2):
        return 1.0 - _beta_incompleta(b, a, 1.0 - x)
    frente = math.exp(math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
                      + a * math.log(x) + b * math.log(1.0 - x)) / a
    minimo = 1e-300
    c, d = 1.0, 1.0 - (a + b) * x / (a + 1)
    d = 1.0 / (d if abs(d) > minimo else minimo)
    f = d
    for m in range(1, 500):
        for passo in (0, 1):
            if passo == 0:
                num = m * (b - m) * x / ((a + 2 * m - 1) * (a + 2 * m))
            else:
                num = -(a + m) * (a + b + m) * x / ((a + 2 * m) * (a + 2 * m + 1))
            d = 1.0 + num * d
            d = 1.0 / (d if abs(d) > minimo else minimo)
            c = 1.0 + num / c
            c = c if abs(c) > minimo else minimo
            f *= c * d
        if abs(c * d - 1.0) < 1e-15:
            break
    return frente * f


def t_acumulada(x, gl):
    if gl <= 0:
        raise ValueError("graus de liberdade precisam ser maiores que zero")
    cauda = 0.5 * _beta_incompleta(gl / 2, 0.5, gl / (gl + x * x))
    return 1.0 - cauda if x >= 0 else cauda


@lru_cache(maxsize=None)
def t_critico(nivel, gl):
    if not 0 < nivel < 1:
        raise ValueError("o nível fica entre 0 e 1, como 0.95")
    alvo = (1 + nivel) / 2
    baixo, alto = 0.0, 1.0
    while t_acumulada(alto, gl) < alvo:
        alto *= 2
    for _ in range(80):
        meio = (baixo + alto) / 2
        if t_acumulada(meio, gl) < alvo:
            baixo = meio
        else:
            alto = meio
    return (baixo + alto) / 2
