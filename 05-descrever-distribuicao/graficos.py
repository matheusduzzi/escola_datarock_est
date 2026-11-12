"""Aula «Descrever distribuição»: os gráficos da aula, salvos na pasta saida/.

Rode de dentro da pasta da aula:  python3 graficos.py
Precisa do pandas e do matplotlib (python3 -m pip install matplotlib).
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # salva em arquivo, sem abrir janela
matplotlib.rcParams["text.parse_math"] = False  # "R$" é texto, não fórmula
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from matplotlib import mlab  # noqa: E402  (a conta que o violino usa por dentro)

tiquetes = pd.read_csv("../dados/loja/tiquetes.csv")
loja = tiquetes.loc[tiquetes["canal"] == "loja_fisica", "valor"]
site = tiquetes.loc[tiquetes["canal"] == "site", "valor"]
site_sem_117 = tiquetes.loc[(tiquetes["canal"] == "site") & (tiquetes["id_pedido"] != 117), "valor"]
saida = Path("saida")
saida.mkdir(exist_ok=True)
arquivos = []


def br(x, casas=2):
    return f"{x:,.{casas}f}".replace(",", "_").replace(".", ",").replace("_", ".")


def salvar(fig, nome):
    fig.tight_layout()
    fig.savefig(saida / nome, dpi=120)
    plt.close(fig)
    arquivos.append(nome)


# 1. O histograma que sai sem escolher nada: 10 faixas iguais, do menor ao maior valor.
fig, ax = plt.subplots(figsize=(7, 3.5))
ax.hist(site)
ax.set_title(f"Site (n = {len(site)}), 10 faixas automáticas")
ax.set_xlabel("valor do pedido (R$)")
ax.set_ylabel("pedidos")
salvar(fig, "1-histograma-padrao.png")

# 2. Faixas de R$ 25, de 0 a 400. O pedido de R$ 38.400,00 fica fora e vai escrito no título.
faixas = list(range(0, 425, 25))
fig, eixos = plt.subplots(2, 1, figsize=(7, 5), sharex=True)
for ax, nome, v in [(eixos[0], "Loja física", loja), (eixos[1], "Site", site)]:
    ax.hist(v, bins=faixas)
    fora = int((v >= 400).sum())
    ax.set_title(f"{nome} (n = {len(v)})" + (f": {fora} pedido acima de R$ 400 fora do gráfico" if fora else ""))
    ax.set_ylabel("pedidos")
eixos[1].set_xlabel("valor do pedido (R$), faixas de R$ 25")
salvar(fig, "2-histograma-faixas-25.png")

# 3. Boxplot dos dois canais. O eixo vai até R$ 400; o pedido de R$ 38.400,00 fica acima do corte.
fig, ax = plt.subplots(figsize=(7, 3.5))
ax.boxplot([loja, site], vert=False, whis=1.5)
ax.set_yticks([1, 2], [f"loja física (n = {len(loja)})", f"site (n = {len(site)})"])
ax.set_xlim(0, 400)
ax.set_title("Bigode até 1,5 IQR. Eixo cortado em R$ 400: 1 pedido do site acima", fontsize=10)
ax.set_xlabel("valor do pedido (R$)")
salvar(fig, "3-boxplot.png")

# 4. Violino do site com e sem o pedido 117, e da loja física. Mediana ligada (showmedians=True).
fig, eixos = plt.subplots(1, 3, figsize=(9, 3.8))
for ax, titulo, v in [(eixos[0], "site, com o 117", site), (eixos[1], "site, sem o 117", site_sem_117),
                      (eixos[2], "loja física", loja)]:
    ax.violinplot([v], showmedians=True)
    ax.set_title(f"{titulo} (n = {len(v)})", fontsize=10)
    ax.set_xticks([])
eixos[0].set_ylabel("valor do pedido (R$)")
salvar(fig, "4-violino.png")

# 5. O exemplo à mão: Ana e Beto, nove vendas cada, com a largura padrão e com largura de R$ 8.
ana = [10, 20, 30, 40, 50, 60, 70, 80, 90]
beto = [10, 28, 30, 32, 50, 68, 70, 72, 90]
fig, eixos = plt.subplots(1, 2, figsize=(7, 3.8), sharey=True)
for ax, titulo, largura in [(eixos[0], "largura padrão (Scott)", None), (eixos[1], "largura de R$ 8", 8)]:
    for pos, v in [(1, ana), (2, beto)]:
        fator = None if largura is None else largura / pd.Series(v).std()
        ax.violinplot([v], positions=[pos], bw_method=fator, showmedians=True)
    ax.set_xticks([1, 2], ["Ana (n = 9)", "Beto (n = 9)"])
    ax.set_title(titulo, fontsize=10)
eixos[0].set_ylabel("valor da venda (R$)")
salvar(fig, "5-violino-ana-beto.png")

print(f"matplotlib {matplotlib.__version__}: {len(arquivos)} gráficos em saida/")
for nome in arquivos:
    print(f"  {nome}")

print("\nBeto: altura do violino em R$ 30, R$ 50 e R$ 70 (densidade x 1000)")
for rotulo, largura in [("largura padrão", None), ("largura de R$ 8", 8)]:
    v = np.array(beto, dtype=float)
    kde = mlab.GaussianKDE(v, None if largura is None else largura / v.std(ddof=1))
    h = kde.evaluate(np.array([30.0, 50.0, 70.0])) * 1000
    print(f"  {rotulo} (R$ {br(float(np.sqrt(kde.covariance[0, 0])))}): "
          + " | ".join(f"R$ {x}: {br(float(y))}" for x, y in zip((30, 50, 70), h)))
