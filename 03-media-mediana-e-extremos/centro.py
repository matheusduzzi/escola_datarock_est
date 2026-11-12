"""As contas da aula «Média, mediana e extremos».

Rode de dentro da pasta dessa aula:  python3 centro.py

O que cada parte calcula:
1. Quantos pedidos há em cada canal.
2. Média e mediana dos pedidos do site, quantos passam da média e os três maiores pedidos.
3. As mesmas contas sem o pedido 117, para ver o que um pedido só faz com cada medida.
4. O resumo por canal: quantidade, média, mediana, desvio padrão e a distância entre média e
   mediana, em porcentagem da mediana.
5. Amostras sorteadas de 60 pedidos do site, como se os 241 fossem todos os pedidos: em cada
   uma, a média e a mediana. O sorteio parte sempre do mesmo ponto, então a saída sai igual
   toda vez.
"""
from pathlib import Path

import numpy as np
import pandas as pd

DADOS = Path("../dados/loja/tiquetes.csv")
ID_GRANDE = 117
TAMANHO = 60
SORTEIOS = 1000


def reais(x):
    """Valor em reais no jeito brasileiro: R$ 38.400,00."""
    texto = f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {texto}"


def pct(x):
    return f"{x * 100:.1f}%".replace(".", ",")


tiquetes = pd.read_csv(DADOS)
site = tiquetes[tiquetes["canal"] == "site"]
valor = site["valor"]

print(f"Tíquetes: {len(tiquetes)} pedidos")
print(f"  site {len(site)} | loja física {int((tiquetes['canal'] == 'loja_fisica').sum())}")
print()

print(f"Pedidos do site ({len(valor)})")
print(f"  média    {reais(valor.mean())}")
print(f"  mediana  {reais(valor.median())}")
print(f"  pedidos acima da média: {int((valor > valor.mean()).sum())} de {len(valor)}")
print("  os três maiores:")
for _, linha in site.sort_values("valor", ascending=False).head(3).iterrows():
    print(f"    pedido {int(linha['id_pedido']):>3}  {reais(linha['valor'])}")
print()

sem = site[site["id_pedido"] != ID_GRANDE]["valor"]
print(f"Site sem o pedido {ID_GRANDE} ({len(sem)} pedidos)")
print(f"  média    {reais(sem.mean())}")
print(f"  mediana  {reais(sem.median())}")
print(f"  pedidos acima da média: {int((sem > sem.mean()).sum())} de {len(sem)}")
print()

print("Por canal")
print("  canal          n   média         mediana       desvio padrão   distância")
for canal, grupo in tiquetes.groupby("canal"):
    v = grupo["valor"]
    distancia = abs(v.mean() - v.median()) / v.median()
    nome = "loja física" if canal == "loja_fisica" else canal
    print(f"  {nome:<12} {len(v):>3}   {reais(v.mean()):<13} {reais(v.median()):<13} "
          f"{reais(v.std()):<15} {pct(distancia)}")
print()

print(f"Se os {len(valor)} fossem todos os pedidos do site: amostras de {TAMANHO}")
rng = np.random.default_rng(3)
for i in range(1, 6):
    amostra = site.sample(TAMANHO, random_state=rng)
    tem = "  (tem o 117)" if ID_GRANDE in set(amostra["id_pedido"]) else ""
    print(f"  amostra {i}: média {reais(amostra['valor'].mean()):<12} "
          f"mediana {reais(amostra['valor'].median())}{tem}")
medias, medianas, com = [], [], 0
for _ in range(SORTEIOS):
    amostra = site.sample(TAMANHO, random_state=rng)
    medias.append(amostra["valor"].mean())
    medianas.append(amostra["valor"].median())
    com += ID_GRANDE in set(amostra["id_pedido"])
print(f"  em {SORTEIOS} amostras de {TAMANHO}, {com} tiveram o pedido {ID_GRANDE}:")
print(f"    a média foi de {reais(min(medias))} a {reais(max(medias))}")
print(f"    a mediana foi de {reais(min(medianas))} a {reais(max(medianas))}")
