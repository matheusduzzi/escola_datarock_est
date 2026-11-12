"""Espalhamento das entregas da Rápida e da Via Sul em outubro.

Rode de dentro da pasta da aula:  python3 dispersao.py
Lê dados/entregas_outubro.csv e mostra, para cada transportadora, o centro, o espalhamento
e quantas entregas passam de 72 horas. Depois mostra as mesmas medidas em dias, o que uma
entrega perdida faz com o desvio e com o IQR, e de onde vem o n - 1 da variância.
"""
import random

import pandas as pd

PROMESSA = 72  # horas: a loja promete entrega em até 3 dias


def br(x, casas=1):
    """Número com vírgula decimal e ponto de milhar."""
    texto = f"{x:,.{casas}f}"
    return texto.replace(",", "X").replace(".", ",").replace("X", ".")


def medidas(horas):
    q1 = horas.quantile(0.25)
    q3 = horas.quantile(0.75)
    return {
        "n": len(horas),
        "media": horas.mean(),
        "mediana": horas.median(),
        "minimo": horas.min(),
        "maximo": horas.max(),
        "variancia": horas.var(),   # divide por n - 1
        "desvio": horas.std(),      # raiz da variância
        "q1": q1,
        "q3": q3,
        "iqr": q3 - q1,
        "cv": horas.std() / horas.mean(),
    }


entregas = pd.read_csv("dados/entregas_outubro.csv")
nomes = {"rapida": "Rápida", "via_sul": "Via Sul"}
grupos = {t: entregas.loc[entregas["transportadora"] == t, "horas"] for t in nomes}

print(f"Entregas de outubro: {len(entregas)}")
for t, nome in nomes.items():
    print(f"  {nome} {len(grupos[t])}", end="")
print("\n")

print("Horas do pedido até a entrega")
print(f"  {'':22}{'Rápida':>12}{'Via Sul':>12}")
m = {t: medidas(h) for t, h in grupos.items()}
linhas = [
    ("média", "media", 2), ("mediana", "mediana", 2),
    ("mais rápida", "minimo", 1), ("mais lenta", "maximo", 1),
    ("variância (h²)", "variancia", 2), ("desvio padrão", "desvio", 2),
    ("1º quartil", "q1", 3), ("3º quartil", "q3", 3), ("IQR", "iqr", 3),
]
for rotulo, chave, casas in linhas:
    print(f"  {rotulo:22}{br(m['rapida'][chave], casas):>12}{br(m['via_sul'][chave], casas):>12}")
print(f"  {'coef. de variação':22}{br(100 * m['rapida']['cv']) + '%':>12}{br(100 * m['via_sul']['cv']) + '%':>12}")
acima = {t: int((h > PROMESSA).sum()) for t, h in grupos.items()}
print(f"  {'acima de 72 h':22}{str(acima['rapida']) + ' de 60':>12}{str(acima['via_sul']) + ' de 60':>12}")

print("\nAs mesmas entregas em dias (horas ÷ 24)")
for t, nome in nomes.items():
    d = medidas(grupos[t] / 24)
    print(f"  {nome:8} média {br(d['media'], 2)} | desvio {br(d['desvio'], 2)} | "
          f"variância {br(d['variancia'], 3)} | IQR {br(d['iqr'], 3)} | CV {br(100 * d['cv'])}%")

print("\nUma entrega da Rápida se perde e chega com 200 h")
com_perdida = pd.concat([grupos["rapida"], pd.Series([200.0])], ignore_index=True)
p = medidas(com_perdida)
print(f"  {'':10}{'desvio':>10}{'IQR':>10}{'média':>10}{'mediana':>10}")
print(f"  {'60 entregas':10}{br(m['rapida']['desvio'], 2):>10}{br(m['rapida']['iqr'], 3):>10}"
      f"{br(m['rapida']['media'], 2):>10}{br(m['rapida']['mediana'], 2):>10}")
print(f"  {'61 entregas':10}{br(p['desvio'], 2):>10}{br(p['iqr'], 3):>10}"
      f"{br(p['media'], 2):>10}{br(p['mediana'], 2):>10}")

print("\nDe onde vem o n - 1: as 60 entregas da Via Sul como se fossem todas")
populacao = grupos["via_sul"].tolist()
N = len(populacao)
mu = sum(populacao) / N
sigma2 = sum((x - mu) ** 2 for x in populacao) / N
print(f"  variância das 60, dividindo por 60: {br(sigma2, 2)} h²")
sorteio = random.Random(4)
por_n, por_n1 = [], []
for _ in range(10_000):
    amostra = sorteio.choices(populacao, k=5)
    media_amostra = sum(amostra) / 5
    soma_quadrados = sum((x - media_amostra) ** 2 for x in amostra)
    por_n.append(soma_quadrados / 5)
    por_n1.append(soma_quadrados / 4)
print("  10.000 amostras de 5 entregas, sorteadas com reposição:")
print(f"    média das variâncias dividindo por 5 (n):     {br(sum(por_n) / len(por_n), 2)} h²")
print(f"    média das variâncias dividindo por 4 (n - 1): {br(sum(por_n1) / len(por_n1), 2)} h²")
