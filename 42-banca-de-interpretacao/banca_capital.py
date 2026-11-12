"""As perguntas da banca sobre a nota da capital, com o piloto de setembro.

    python3 banca_capital.py

É o comando que vai na nota final: quem lê roda de novo e vê os mesmos números.
Junta os blocos das seções 4 a 9 da aula, na mesma ordem. Só biblioteca padrão.
As regras são as da nota da aula 41, escritas antes dos dados:
- a troca paga se a nova for pelo menos 3 horas mais rápida na média, com a faixa de 98%
  (conta da Dani em maio: cada hora a menos vale R$ 0,50 por entrega em reclamação evitada);
- a loja mostra um prazo se a faixa de Wilson de 95% da parte que chega nele começa em 90% ou
  mais (regra da Marta em agosto).
"""
import csv
import math
from pathlib import Path
from statistics import mean, variance

from distribuicao_t import t_critico

PASTA = Path(__file__).resolve().parent
NIVEL_DA_TROCA = 0.98
GANHO_MINIMO = 3          # horas
REAIS_POR_HORA = 0.50     # por entrega, conta da Dani em maio
PARTE_MINIMA = 0.90       # 9 em cada 10 entregas no prazo mostrado
PRAZOS = [54, 60]


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


def minimo_no_prazo(n, minimo=PARTE_MINIMA):
    """Menor número de entregas no prazo, entre n, para a faixa começar no mínimo. None se nem n de n basta."""
    return next((k for k in range(n + 1) if wilson(k, n)[0] >= minimo), None)


def aguenta_sem_baixa(x, prazo, minimo=PARTE_MINIMA):
    """Quantas entregas sem baixa, todas atrasadas, a regra aguenta. None se o prazo já não passa sem elas."""
    k = sum(1 for h in x if h <= prazo)
    precisa = minimo_no_prazo(len(x), minimo)
    if precisa is None or k < precisa:
        return None
    v = 0
    while True:
        precisa = minimo_no_prazo(len(x) + v + 1, minimo)
        if precisa is None or precisa > k:
            return v
        v += 1


def aguenta_atraso(x, prazo, minimo=PARTE_MINIMA):
    """Quantas horas a mais em cada entrega o prazo aguenta. None se ele já não passa."""
    precisa = minimo_no_prazo(len(x), minimo)
    if precisa is None:
        return None
    folga = prazo - sorted(x)[precisa - 1]
    return round(folga, 1) if folga >= 0 else None


def vale_por_pelo_menos(x, prazo, minimo=PARTE_MINIMA):
    """Menor número de entregas independentes que a mesma parte no prazo precisa para passar. None se não passa."""
    p = sum(1 for h in x if h <= prazo) / len(x)
    n = len(x)
    if wilson(p * n, n)[0] < minimo:
        return None
    while n > 1 and wilson(p * (n - 1), n - 1)[0] >= minimo:
        n -= 1
    return n


def ler_setembro():
    with open(PASTA / "setembro.csv", encoding="utf-8") as f:
        setembro = list(csv.DictReader(f))
    vazias = [l["id_entrega"] for l in setembro if l["horas"].strip() == ""]
    horas = {t: [float(l["horas"]) for l in setembro if l["transportadora"] == t] for t in ("atual", "nova")}
    return setembro, vazias, horas


def main():
    setembro, vazias, horas = ler_setembro()
    print("piloto de setembro, capital:", len(setembro), "entregas; sem baixa:", vazias)

    ganho, baixo, alto = welch(horas["atual"], horas["nova"], NIVEL_DA_TROCA)
    print("1. a nota: a nova foi", round(ganho, 2), "h mais rápida; faixa de 98% de", round(baixo, 2), "a",
          round(alto, 2), "h; paga as", GANHO_MINIMO, "h?", decidir(baixo, alto, GANHO_MINIMO))
    for t, x in horas.items():
        k = sum(1 for h in x if h <= 54)
        a, b = wilson(k, len(x))
        print("  ", t, "até 54 h:", k, "de", len(x), "de", pct(a), "a", pct(b), "% ->", decidir(a, b, PARTE_MINIMA))

    print("2. o preço da nova (cada R$", REAIS_POR_HORA, "por entrega pede 1 hora a menos)")
    for preco in [2.50, 1.50, 1.00, 0.70]:
        limite = preco / REAIS_POR_HORA
        print("   R$", preco, "pede", round(limite, 2), "h ->", decidir(baixo, alto, limite))
    centavos = range(1, 301)
    sim = [c for c in centavos if decidir(baixo, alto, c / 100 / REAIS_POR_HORA) == "sim"]
    nao = [c for c in centavos if decidir(baixo, alto, c / 100 / REAIS_POR_HORA) == "não"]
    print("   sim até", max(sim), "centavos; não a partir de", min(nao), "centavos; começo da faixa sem arredondar:",
          round(baixo, 3))

    print("3. o nível da faixa da troca")
    for nivel in [0.98, 0.95, 0.90]:
        _, de, ate = welch(horas["atual"], horas["nova"], nivel)
        print("  ", nivel, "de", round(de, 2), "a", round(ate, 2), "h ->", decidir(de, ate, GANHO_MINIMO))

    print("4. entregas sem baixa que o prazo aguenta, todas atrasadas; mínimo no prazo com 105:", minimo_no_prazo(105))
    for t, x in horas.items():
        print("  ", t, {p: aguenta_sem_baixa(x, p) for p in PRAZOS})

    print("5. horas a mais em cada entrega que o prazo aguenta")
    for t, x in horas.items():
        print("  ", t, "entrega número", minimo_no_prazo(len(x)), "das mais rápidas:",
              sorted(x)[minimo_no_prazo(len(x)) - 1], "h;", {p: aguenta_atraso(x, p) for p in PRAZOS})

    print("6. as 105 entregas precisam valer por pelo menos")
    for t, x in horas.items():
        print("  ", t, {p: vale_por_pelo_menos(x, p) for p in PRAZOS})


if __name__ == "__main__":
    main()
