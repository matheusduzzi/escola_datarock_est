"""A tabela F no Python, só com a biblioteca padrão.

f_acumulada(x, gl1, gl2) é a chance de um valor da distribuição F com gl1 e gl2 graus de
liberdade ficar abaixo de x. A chance de ficar acima, 1 - f_acumulada(x, gl1, gl2), é o
p-valor do teste F. f_critico(alfa, gl1, gl2) é o número da tabela F: só alfa dos valores
ficam acima dele (0.05 dá o da tabela de 5%). Os graus de liberdade podem ter vírgula,
como o gl2 da ANOVA de Welch.
No SciPy, a mesma conta é scipy.stats.f.cdf(x, gl1, gl2) e scipy.stats.f.ppf(1 - alfa, gl1, gl2).
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


def f_acumulada(x, gl1, gl2):
    if gl1 <= 0 or gl2 <= 0:
        raise ValueError("graus de liberdade precisam ser maiores que zero")
    if x <= 0:
        return 0.0
    return _beta_incompleta(gl1 / 2, gl2 / 2, gl1 * x / (gl1 * x + gl2))


@lru_cache(maxsize=None)
def f_critico(alfa, gl1, gl2):
    if not 0 < alfa < 1:
        raise ValueError("o alfa fica entre 0 e 1, como 0.05")
    alvo = 1 - alfa
    baixo, alto = 0.0, 1.0
    while f_acumulada(alto, gl1, gl2) < alvo:
        alto *= 2
    for _ in range(80):
        meio = (baixo + alto) / 2
        if f_acumulada(meio, gl1, gl2) < alvo:
            baixo = meio
        else:
            alto = meio
    return (baixo + alto) / 2
