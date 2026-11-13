"""Desenha o gráfico de dispersão de duas colunas, com uma cor por segmento, e salva em saidas/.

Precisa do Matplotlib (python3 -m pip install matplotlib). Rode de dentro da pasta da aula:

    python3 dispersao.py                                    # pedidos de setembro: distância x valor, por canal
    python3 dispersao.py --destacar 1150                    # marca o pedido 1150 com um anel e o id
    python3 dispersao.py --sem 1150                         # desenha sem o pedido 1150
    python3 dispersao.py --arquivo dados/entregas_maio.csv --x volumes --y horas --segmento modalidade

O que cada parte faz:
- matplotlib.use("Agg"): o gráfico vai direto para um arquivo PNG, sem abrir janela.
- fig, ax = plt.subplots(): cria a figura e a área com os eixos.
- ax.scatter(x, y): um ponto por linha. O programa chama uma vez por segmento, e cada chamada
  ganha uma cor e um formato de marcador, com o nome do segmento na legenda.
- --destacar: desenha um anel em volta da linha com esse id e escreve o id ao lado.
- fig.savefig(...): salva em saidas/dispersao_<x>_<y>.png (ou com _sem_<ids> no fim).
"""
import argparse
import sys
from pathlib import Path

import pandas as pd

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    sys.exit("Esse programa precisa do Matplotlib. Instale com: python3 -m pip install matplotlib")

AQUI = Path(__file__).resolve().parent
MARCADORES = ["o", "s", "^", "D", "v", "P"]
CORES = ["#52645C", "#C8962E", "#3B6EA8", "#A2453D", "#6B5B95", "#2F8F83"]


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--arquivo", default="dados/pedidos_setembro.csv")
    p.add_argument("--x", default="distancia_km")
    p.add_argument("--y", default="valor")
    p.add_argument("--segmento", default="canal", help='coluna dos grupos; "nenhum" para uma cor só')
    p.add_argument("--sem", action="append", default=[], metavar="ID", help="tira a linha com esse id (pode repetir)")
    p.add_argument("--destacar", action="append", default=[], metavar="ID", help="marca a linha com esse id")
    p.add_argument("--saida", default="saidas", help="pasta do PNG (padrão saidas/, ao lado do programa)")
    args = p.parse_args()

    caminho = Path(args.arquivo)
    if not caminho.is_absolute():
        caminho = AQUI / caminho
    if not caminho.is_file():
        sys.exit(f"Arquivo não encontrado: {args.arquivo}")
    tabela = pd.read_csv(caminho)
    segmento = None if args.segmento == "nenhum" else args.segmento
    for nome, col in [("--x", args.x), ("--y", args.y), ("--segmento", segmento)]:
        if col is not None and col not in tabela.columns:
            sys.exit(f"{nome}: a coluna '{col}' não existe em {args.arquivo}. Colunas: {', '.join(tabela.columns)}")
    for col in (args.x, args.y):
        if not pd.api.types.is_numeric_dtype(tabela[col]):
            sys.exit(f"A coluna '{col}' precisa ser numérica para o gráfico.")
    ids = [c for c in tabela.columns if c.lower().startswith("id")]
    if (args.sem or args.destacar) and not ids:
        sys.exit("--sem e --destacar precisam de uma coluna de id no arquivo.")
    col_id = ids[0] if ids else None
    for valor in args.sem + args.destacar:
        if not (tabela[col_id].astype(str) == valor).any():
            sys.exit(f"Não há linha com {col_id} = {valor} em {args.arquivo}")
    if args.sem:
        tabela = tabela[~tabela[col_id].astype(str).isin(args.sem)]
    tabela = tabela.dropna(subset=[args.x, args.y])

    fig, ax = plt.subplots(figsize=(8, 5), dpi=120)
    grupos = [(str(n), g) for n, g in tabela.groupby(segmento)] if segmento else [("todas", tabela)]
    for i, (nome, g) in enumerate(grupos):
        ax.scatter(g[args.x], g[args.y], s=28, alpha=0.8, marker=MARCADORES[i % len(MARCADORES)],
                   color=CORES[i % len(CORES)], label=f"{nome} ({len(g)})")
    for valor in args.destacar:
        linha = tabela[tabela[col_id].astype(str) == valor]
        if linha.empty:
            continue
        x, y = float(linha[args.x].iloc[0]), float(linha[args.y].iloc[0])
        ax.scatter([x], [y], s=220, facecolors="none", edgecolors="black", linewidths=1.5)
        ax.annotate(f"{col_id} {valor}", (x, y), xytext=(8, -14), textcoords="offset points")
    ax.set_xlabel(args.x)
    ax.set_ylabel(args.y)
    ax.set_title(f"{caminho.name}: {args.y} contra {args.x}" + (f", sem {', '.join(args.sem)}" if args.sem else ""))
    if segmento:
        ax.legend(title=segmento)
    ax.grid(alpha=0.3)

    pasta = Path(args.saida)
    if not pasta.is_absolute():
        pasta = AQUI / pasta
    pasta.mkdir(parents=True, exist_ok=True)
    nome = f"dispersao_{args.x}_{args.y}" + (f"_sem_{'_'.join(args.sem)}" if args.sem else "") + ".png"
    fig.savefig(pasta / nome, bbox_inches="tight")
    print(f"salvo: {pasta.name}/{nome} | {len(tabela)} pontos | grupos: "
          + ", ".join(f"{n} {len(g)}" for n, g in grupos))
    return 0


if __name__ == "__main__":
    sys.exit(main())
