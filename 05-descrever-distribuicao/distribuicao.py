"""Aula «Descrever distribuição»: os números por trás de quantis, histograma, boxplot e violino.

Rode de dentro da pasta da aula:  python3 distribuicao.py
Só precisa do pandas. Os gráficos estão no graficos.py.
"""
import numpy as np
import pandas as pd

tiquetes = pd.read_csv("../dados/loja/tiquetes.csv")
NOME = {"loja_fisica": "loja física", "site": "site"}
CANAIS = ["loja_fisica", "site"]
valores = {c: tiquetes.loc[tiquetes["canal"] == c, "valor"] for c in CANAIS}


def br(x, casas=2):
    """Número no formato brasileiro: 38.400,00."""
    return f"{x:,.{casas}f}".replace(",", "_").replace(".", ",").replace("_", ".")


def metades(v):
    """Quartis pela mediana de cada metade (com n ímpar, a mediana fica fora das metades)."""
    s = sorted(v)
    n = len(s)
    baixo, cima = s[: n // 2], s[(n + 1) // 2:]
    return float(np.median(baixo)), float(np.median(cima))


def quartis(v):
    """Q1 e Q3 em cada convenção. As cinco primeiras são do pandas; weibull é do NumPy."""
    q = {}
    for m in ["linear", "lower", "higher", "nearest", "midpoint"]:
        q[m] = tuple(float(v.quantile(p, interpolation=m)) for p in (0.25, 0.75))
    q["weibull"] = tuple(float(x) for x in np.quantile(np.asarray(v), [0.25, 0.75], method="weibull"))
    q["metades"] = metades(v)
    return q


print(f"Tíquetes: {len(tiquetes)} pedidos")
print(f"  site {len(valores['site'])} | loja física {len(valores['loja_fisica'])}")

print('\nQuantis (convenção do pandas: interpolation="linear")')
print(f"  {'canal':<12}{'n':>4}{'5%':>9}{'25%':>9}{'50%':>9}{'75%':>9}{'95%':>9}{'maior':>11}")
for c in CANAIS:
    v = valores[c]
    q = [br(v.quantile(p)) for p in (0.05, 0.25, 0.5, 0.75, 0.95)]
    print(f"  {NOME[c]:<12}{len(v):>4}" + "".join(f"{x:>9}" for x in q) + f"{br(v.max()):>11}")

oito = pd.Series([80, 95, 100, 110, 120, 140, 150, 300], dtype=float)
rotulo = {"linear": "linear (pandas, padrão)", "lower": "lower", "higher": "higher", "nearest": "nearest",
          "midpoint": "midpoint", "weibull": "weibull (NumPy)", "metades": "mediana de cada metade"}
print("\nOito pedidos, sete convenções de quartil")
print("  valores: " + " ".join(str(int(x)) for x in oito))
print(f"  {'convenção':<26}{'Q1':>8}{'Q3':>9}")
for m, (q1, q3) in quartis(oito).items():
    print(f"  {rotulo[m]:<26}{br(q1):>8}{br(q3):>9}")

print("\nAs mesmas sete convenções nos tíquetes")
for c in CANAIS:
    q = quartis(valores[c]).values()
    q1s, q3s = [a for a, _ in q], [b for _, b in q]
    print(f"  {NOME[c] + f' ({len(valores[c])})':<18} Q1 de {br(min(q1s))} a {br(max(q1s))} | "
          f"Q3 de {br(min(q3s))} a {br(max(q3s))}")

site = valores["site"]
contagem, bordas = np.histogram(site, bins=10)
print("\nHistograma do site com 10 faixas iguais, do menor ao maior valor (o padrão do matplotlib)")
print(f"  largura de cada faixa: R$ {br(bordas[1] - bordas[0])}")
print(f"  faixa 1, de R$ {br(bordas[0])} a R$ {br(bordas[1])}: {contagem[0]} pedidos")
print(f"  faixas 2 a 9: {contagem[1:9].sum()} pedidos")
print(f"  faixa 10, de R$ {br(bordas[9])} a R$ {br(bordas[10])}: {contagem[9]} pedido")

faixas = list(range(0, 425, 25))
fora = {c: valores[c][valores[c] >= 400] for c in CANAIS}
print("\nFaixas de R$ 25, de R$ 0 a R$ 400 (cada faixa inclui o começo e não inclui o fim)")
print(f"  {'faixa':<14}{'loja física':>12}{'site':>7}")
cont = {c: pd.cut(valores[c], bins=faixas, right=False).value_counts(sort=False).tolist() for c in CANAIS}
for i in range(len(faixas) - 1):
    print(f"  {f'{faixas[i]} a {faixas[i + 1]}':<14}{cont['loja_fisica'][i]:>12}{cont['site'][i]:>7}")
for c in CANAIS:
    lista = ", ".join(f"R$ {br(x)}" for x in fora[c])
    print(f"  fora do gráfico, {NOME[c]}: {len(fora[c])}" + (f" ({lista})" if lista else ""))

print("\nBoxplot (bigode até 1,5 IQR além da caixa, o padrão do matplotlib)")
print(f"  {'':<18}{'loja física':>12}{'site':>10}")
linhas = {k: [] for k in ["Q1", "mediana", "Q3", "IQR", "cerca de baixo", "cerca de cima",
                          "bigode de baixo", "bigode de cima", "pontos fora"]}
for c in CANAIS:
    v = valores[c]
    q1, q3 = v.quantile(0.25), v.quantile(0.75)
    iqr = q3 - q1
    baixo, cima = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    for k, x in [("Q1", q1), ("mediana", v.median()), ("Q3", q3), ("IQR", iqr), ("cerca de baixo", baixo),
                 ("cerca de cima", cima), ("bigode de baixo", v[v >= baixo].min()),
                 ("bigode de cima", v[v <= cima].max())]:
        linhas[k].append(br(x))
    linhas["pontos fora"].append(str(int(((v < baixo) | (v > cima)).sum())))
for k, (a, b) in linhas.items():
    print(f"  {k:<18}{a:>12}{b:>10}")

print("\nViolino: largura da suavização (regra de Scott, o padrão do matplotlib)")
print("  largura = desvio padrão x n elevado a -1/5")
sem117 = site[tiquetes.loc[site.index, "id_pedido"] != 117]
grupos = [("loja física", valores["loja_fisica"]), ("site", site), ("site sem o pedido 117", sem117)]
for nome, v in grupos:
    print(f"  {nome + f' ({len(v)})':<28} R$ {br(v.std() * len(v) ** -0.2):>8}")
print("  o matplotlib desenha a forma em 100 pontos, do menor ao maior valor:")
for nome, v in grupos[1:]:
    print(f"    {nome}: um ponto a cada R$ {br((v.max() - v.min()) / 99)}")
