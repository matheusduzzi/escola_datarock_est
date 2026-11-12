"""As contas da aula «Investigar valores extremos».

Rode de dentro da pasta da aula:  python3 extremos.py

1. Um exemplo pequeno: cerca do IQR e z-score em dez pedidos.
2. Os tíquetes do site: o que cada regra marca, com e sem o pedido 117.
3. Os pedidos de novembro: o que cada regra marca e o que a nota fiscal diz de cada um.
4. Sensibilidade: o tíquete típico e o total em cada decisão.
"""
import pandas as pd


def cercas_iqr(valores, k=1.5):
    """Cerca de baixo e de cima: 1,5 IQR além do 1º e do 3º quartil (quartil padrão do pandas)."""
    q1, q3 = valores.quantile(0.25), valores.quantile(0.75)
    iqr = q3 - q1
    return q1 - k * iqr, q3 + k * iqr


def fora_da_cerca(valores, k=1.5):
    baixo, cima = cercas_iqr(valores, k)
    return (valores < baixo) | (valores > cima)


def z_scores(valores):
    """Quantos desvios padrão cada valor fica da média (desvio do pandas, n - 1)."""
    return (valores - valores.mean()) / valores.std()


def num(x, casas=2):
    return f"{x:,.{casas}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def reais(x):
    return "R$ " + num(x)


# 1. Exemplo pequeno
dez = pd.Series([80, 90, 100, 110, 120, 130, 140, 150, 160, 1200], dtype=float)
baixo, cima = cercas_iqr(dez)
z = z_scores(dez)
print("1. Dez pedidos: 80, 90, 100, 110, 120, 130, 140, 150, 160 e 1.200")
print(f"  1º quartil {num(dez.quantile(0.25))} | 3º quartil {num(dez.quantile(0.75))} | "
      f"IQR {num(dez.quantile(0.75) - dez.quantile(0.25))}")
print(f"  cercas {num(baixo)} e {num(cima)} | fora da cerca: {num(dez[fora_da_cerca(dez)].iloc[0], 0)}")
print(f"  média {num(dez.mean())} | desvio {num(dez.std())} | z do 1.200: {num(z.iloc[-1])}")
for grande in (12000, 120000):
    outro = dez.copy()
    outro.iloc[-1] = grande
    print(f"  trocando 1.200 por {num(grande, 0)}: z {num(z_scores(outro).iloc[-1])}")
print(f"  maior z possível com 10 valores: (10 - 1) / raiz de 10 = {num(9 / 10 ** 0.5)}")

# 2. Tíquetes do site
tiquetes = pd.read_csv("../dados/loja/tiquetes.csv")
site = tiquetes.loc[tiquetes["canal"] == "site"].set_index("id_pedido")["valor"]
print()
print("2. Tíquetes do site")
for rotulo, v in (("com o 117", site), ("sem o 117", site.drop(117))):
    baixo, cima = cercas_iqr(v)
    zz = z_scores(v)
    marcados_z = v[zz.abs() > 3]
    print(f"  {rotulo} ({len(v)} pedidos): média {reais(v.mean())} | desvio {reais(v.std())}")
    print(f"    cerca do IQR: {reais(baixo)} a {reais(cima)} | fora da cerca: {fora_da_cerca(v).sum()}")
    print(f"    |z| > 3: {len(marcados_z)} | "
          + ", ".join(f"pedido {i} {reais(x)} (z {num(zz[i])})" for i, x in marcados_z.items()))
    print(f"    z do pedido 288 ({reais(site[288])}): {num(zz[288])}")

# 3. Pedidos de novembro
pedidos = pd.read_csv("dados/pedidos_novembro.csv")
notas = pd.read_csv("dados/notas_novembro.csv")
nov = pedidos.merge(notas, on="id_pedido", how="left").set_index("id_pedido")
valor = nov["valor"]
iqr_marca = fora_da_cerca(valor)
zz = z_scores(valor)
z_marca = zz.abs() > 3
baixo, cima = cercas_iqr(valor)
print()
print(f"3. Pedidos do site de novembro: {len(nov)} | notas fiscais: {len(notas)}")
print(f"  mediana {reais(valor.median())} | média {reais(valor.mean())} | desvio {reais(valor.std())}")
print(f"  cerca do IQR: {reais(baixo)} a {reais(cima)} | fora da cerca: {iqr_marca.sum()} | "
      f"|z| > 3: {z_marca.sum()}")
print("  pedido  itens          valor       z  cerca  |z|>3  nota fiscal")
for i in nov.index[iqr_marca | z_marca]:
    linha = nov.loc[i]
    nota = "sem nota" if pd.isna(linha["valor_nota"]) else reais(linha["valor_nota"])
    print(f"  {i}  {int(linha['itens']):>5}  {reais(linha['valor']):>13}  {num(zz[i]):>6}  "
          f"{'fora' if iqr_marca[i] else '-':>5}  {'fora' if z_marca[i] else '-':>5}  {nota}")
diferente = nov[nov["valor_nota"].notna() & (nov["valor"] != nov["valor_nota"])].index.tolist()
sem_nota = nov[nov["valor_nota"].isna()].index.tolist()
print(f"  valor do pedido diferente da nota: {diferente} | pedido sem nota: {sem_nota}")

# 4. Sensibilidade
minha = valor.copy()
minha[5037] = nov.loc[5037, "valor_nota"]
minha = minha.drop(5121)
cenarios = [
    ("como veio", valor),
    ("tira |z| > 3", valor[~z_marca]),
    ("tira fora da cerca", valor[~iqr_marca]),
    ("corrige 5037, mantém 5088, tira 5121", minha),
    ("a mesma, sem o 5088", minha.drop(5088)),
]
print()
print("4. Sensibilidade: o que cada decisão faz com as respostas")
print(f"  {'decisão':<38}{'pedidos':>8}{'mediana':>13}{'média':>13}{'total':>16}")
for nome, v in cenarios:
    print(f"  {nome:<38}{len(v):>8}{reais(v.median()):>13}{reais(v.mean()):>13}{reais(v.sum()):>16}")
