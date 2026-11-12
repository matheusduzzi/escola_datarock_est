"""Os números da nota de decisão da capital, com o piloto de setembro.

    python3 nota_capital.py

É o comando que vai na nota: quem lê roda de novo e vê os mesmos números.
Junta os blocos das seções 3 a 6 da aula, na mesma ordem. Só biblioteca padrão.
As duas regras vêm antes dos dados:
- a troca paga se a nova for pelo menos 3 horas mais rápida na média (conta da Dani em maio);
- a loja mostra um prazo se a faixa de 95% da parte que chega nele começa em 90% ou mais
  (regra da Marta em agosto).
"""
import csv
import math
from pathlib import Path
from statistics import mean, stdev, variance

from distribuicao_t import t_critico

PASTA = Path(__file__).resolve().parent
GANHO_MINIMO = 3       # horas
PARTE_MINIMA = 0.90    # 9 em cada 10 entregas no prazo mostrado
PRAZOS = [48, 54, 60]


def welch(a, b, nivel):
    va, vb = variance(a) / len(a), variance(b) / len(b)
    ep = math.sqrt(va + vb)
    gl = (va + vb) ** 2 / (va ** 2 / (len(a) - 1) + vb ** 2 / (len(b) - 1))
    d = mean(a) - mean(b)
    t = t_critico(nivel, gl)
    return d, d - t * ep, d + t * ep


def decidir(inferior, superior, limite):
    if inferior >= limite:
        return "sim"
    if superior < limite:
        return "não"
    return "inconclusivo"


def wilson(k, n, z=1.96):
    p = k / n
    centro = (p + z**2 / (2 * n)) / (1 + z**2 / n)
    margem = z * math.sqrt(p * (1 - p) / n + z**2 / (4 * n**2)) / (1 + z**2 / n)
    return centro - margem, centro + margem


def pct(x):
    return round(100 * x, 1)


def main():
    with open(PASTA / "setembro.csv", encoding="utf-8") as f:
        setembro = list(csv.DictReader(f))
    vazias = [l["id_entrega"] for l in setembro if l["horas"].strip() == ""]
    horas = {t: [float(l["horas"]) for l in setembro if l["transportadora"] == t] for t in ("atual", "nova")}
    print("piloto de setembro, capital:", len(setembro), "entregas; sem baixa:", vazias)
    for t, x in horas.items():
        print(" ", t, len(x), "entregas, média", round(mean(x), 2), "h, desvio", round(stdev(x), 2))

    ganho, baixo, alto = welch(horas["atual"], horas["nova"], 0.98)
    print("troca: a nova foi", round(ganho, 2), "h mais rápida; faixa de 98% de", round(baixo, 2), "a",
          round(alto, 2), "h; paga as", GANHO_MINIMO, "h?", decidir(baixo, alto, GANHO_MINIMO))

    print("prazo: parte até o prazo, faixa de Wilson de 95%, começa em", pct(PARTE_MINIMA), "% ou mais?")
    for t, x in horas.items():
        for prazo in PRAZOS:
            k = sum(1 for h in x if h <= prazo)
            a, b = wilson(k, len(x))
            print(" ", t, prazo, "h:", k, "de", len(x), "=", pct(k / len(x)), "%, de", pct(a), "a", pct(b),
                  "->", decidir(a, b, PARTE_MINIMA))

    print("uma entrega nova: faixa de previsão de 95%")
    for t, x in horas.items():
        n = len(x)
        margem = t_critico(0.95, n - 1) * stdev(x) * math.sqrt(1 + 1 / n)
        print(" ", t, round(mean(x) - margem, 1), "a", round(mean(x) + margem, 1), "h")


if __name__ == "__main__":
    main()
