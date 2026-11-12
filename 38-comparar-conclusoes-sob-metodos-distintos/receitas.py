"""As receitas das aulas anteriores, prontas para importar. Só a biblioteca padrão.

pareado e welch vêm da aula «Comparar médias independentes e pareadas».
postos, chance_de_ganhar, mann_whitney e permutacao vêm da aula «Métodos não paramétricos e permutação».
As contas são as mesmas das aulas. Aqui todas retornam números arredondados, e pareado e welch
também retornam o p de dois lados.
"""
import math
from collections import Counter
from statistics import NormalDist, mean, stdev, variance

from distribuicao_t import t_acumulada, t_critico


def pareado(difs, nivel=0.95):
    """Faixa t da média das diferenças, uma diferença por par."""
    n = len(difs)
    d = mean(difs)
    ep = stdev(difs) / math.sqrt(n)
    c = t_critico(nivel, n - 1)
    p = 2 * (1 - t_acumulada(abs(d) / ep, n - 1))
    return {"dif": round(d, 2), "baixo": round(d - c * ep, 2), "alto": round(d + c * ep, 2), "p": round(p, 4)}


def welch(x, y, nivel=0.95):
    """Faixa de Welch da diferença das médias de dois grupos independentes, x menos y."""
    vx, vy = variance(x) / len(x), variance(y) / len(y)
    ep = math.sqrt(vx + vy)
    gl = (vx + vy) ** 2 / (vx ** 2 / (len(x) - 1) + vy ** 2 / (len(y) - 1))
    d, c = mean(x) - mean(y), t_critico(nivel, gl)
    p = 2 * (1 - t_acumulada(abs(d) / ep, gl))
    return {"dif": round(d, 2), "baixo": round(d - c * ep, 2), "alto": round(d + c * ep, 2), "p": round(p, 4)}


def postos(valores):
    """Posição de cada valor na fila, do menor para o maior. Empate fica com a média das posições."""
    ordem = sorted(range(len(valores)), key=lambda i: valores[i])
    r = [0.0] * len(valores)
    i = 0
    while i < len(ordem):
        j = i
        while j + 1 < len(ordem) and valores[ordem[j + 1]] == valores[ordem[i]]:
            j += 1
        for k in range(i, j + 1):
            r[ordem[k]] = (i + j) / 2 + 1
        i = j + 1
    return r


def chance_de_ganhar(x, y):
    """Num par sorteado, um valor de cada grupo, a chance de o de x ser maior. Empate vale meio."""
    r = postos(x + y)
    u = sum(r[:len(x)]) - len(x) * (len(x) + 1) / 2
    return u / (len(x) * len(y))


def mann_whitney(x, y):
    """Chance de ganhar e o p do Mann-Whitney pela curva normal, com ajuste para empates."""
    nx, ny = len(x), len(y)
    n = nx + ny
    u = chance_de_ganhar(x, y) * nx * ny
    empates = sum(t ** 3 - t for t in Counter(x + y).values())
    var = nx * ny / 12 * ((n + 1) - empates / (n * (n - 1)))
    z = (abs(u - nx * ny / 2) - 0.5) / math.sqrt(var)
    p = min(1.0, 2 * (1 - NormalDist().cdf(max(z, 0))))
    return {"chance": round(u / (nx * ny), 3), "p": round(p, 4)}


def dif_medias(x, y):
    return mean(x) - mean(y)


def permutacao(x, y, estatistica, vezes, rng):
    """Embaralha as etiquetas entre os dois grupos `vezes` vezes. O p soma 1 em cima e embaixo."""
    real = estatistica(x, y)
    todos, nx = x + y, len(x)
    acima = abaixo = 0
    embaralhado = todos[:]
    for _ in range(vezes):
        rng.shuffle(embaralhado)
        v = estatistica(embaralhado[:nx], embaralhado[nx:])
        acima += v >= real - 1e-9
        abaixo += v <= real + 1e-9
    acima, abaixo = (acima + 1) / (vezes + 1), (abaixo + 1) / (vezes + 1)
    return {"real": round(real, 3), "p": round(min(1.0, 2 * min(acima, abaixo)), 4)}
