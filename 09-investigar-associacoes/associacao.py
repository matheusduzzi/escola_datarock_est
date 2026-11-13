"""Pearson e Spearman de duas colunas, no total e em cada segmento, e as linhas que mais mexem no Pearson.

Rode de dentro da pasta da aula:

    python3 associacao.py                                   # pedidos de setembro: distância x valor, por canal
    python3 associacao.py --sem 1150                        # o mesmo, sem o pedido 1150
    python3 associacao.py --arquivo dados/entregas_maio.csv --x volumes --y horas --segmento modalidade

O que cada parte faz, em pandas:
- total: tabela[[x, y]].corr(method="pearson") e .corr(method="spearman"), com todas as linhas.
- segmentos: as mesmas duas contas dentro de cada valor da coluna de segmento (groupby), com a
  média de x e de y no grupo. Segmento com menos de 3 linhas não ganha correlação.
- linhas que mais mexem: tira uma linha de cada vez, calcula o Pearson do total sem ela e mostra
  as que mais mudam o resultado, para mais ou para menos.
- --sem: tira linhas pelo id (a primeira coluna que começa com "id") antes de todas as contas.
  Pode repetir. A linha some da conta, não do arquivo.

Linhas com vazio em x ou em y saem das contas, e o programa diz quantas foram.
"""
import argparse
import sys
from pathlib import Path

import pandas as pd

AQUI = Path(__file__).resolve().parent


def br(x, casas=1):
    texto = f"{x:,.{casas}f}"
    return texto.replace(",", "_").replace(".", ",").replace("_", ".")


def casas_de(coluna):
    if pd.api.types.is_integer_dtype(coluna):
        return 0
    return 1 if ((coluna * 10).round(6) % 1 == 0).all() else 2


def correlacoes(grupo, x, y):
    if len(grupo) < 3:
        return "-", "-"
    return (br(grupo[[x, y]].corr(method="pearson").iloc[0, 1], 2),
            br(grupo[[x, y]].corr(method="spearman").iloc[0, 1], 2))


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--arquivo", default="dados/pedidos_setembro.csv")
    p.add_argument("--x", default="distancia_km")
    p.add_argument("--y", default="valor")
    p.add_argument("--segmento", default="canal", help='coluna dos grupos; "nenhum" para não separar')
    p.add_argument("--sem", action="append", default=[], metavar="ID", help="tira a linha com esse id (pode repetir)")
    p.add_argument("--influentes", type=int, default=5, help="quantas linhas mostrar no fim (padrão 5)")
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
            sys.exit(f"A coluna '{col}' precisa ser numérica para calcular correlação.")
    if args.influentes < 0:
        sys.exit("--influentes precisa ser 0 ou mais.")
    ids = [c for c in tabela.columns if c.lower().startswith("id")]
    if args.sem and not ids:
        sys.exit("--sem precisa de uma coluna de id no arquivo.")
    col_id = ids[0] if ids else None

    tirados = []
    for valor in args.sem:
        achou = tabela[col_id].astype(str) == valor
        if not achou.any():
            sys.exit(f"--sem: não há linha com {col_id} = {valor} em {args.arquivo}")
        tirados.append(valor)
        tabela = tabela[~achou]
    vazias = int(tabela[[args.x, args.y]].isna().any(axis=1).sum())
    tabela = tabela.dropna(subset=[args.x, args.y])
    if len(tabela) < 3:
        sys.exit("São precisas pelo menos 3 linhas para calcular correlação.")

    print(f"{caminho.name}: {len(tabela)} linhas | x: {args.x} | y: {args.y} | segmento: {segmento or 'nenhum'}")
    if tirados:
        print(f"tiradas das contas: {col_id} " + ", ".join(tirados))
    if vazias:
        print(f"linhas com vazio em {args.x} ou {args.y}, fora das contas: {vazias}")
    print()

    largura = max([5] + ([len(str(v)) for v in tabela[segmento].unique()] if segmento else [])) + 2
    cab_x, cab_y = f"média de {args.x}", f"média de {args.y}"
    print(f"{'grupo':<{largura}} {'linhas':>6}  {cab_x:>{len(cab_x)}}  {cab_y:>{len(cab_y)}}  {'Pearson':>7}  {'Spearman':>8}")
    grupos = [("todas", tabela)]
    if segmento:
        grupos += [(str(nome), g) for nome, g in tabela.groupby(segmento)]
    for nome, g in grupos:
        pe, sp = correlacoes(g, args.x, args.y)
        print(f"{nome:<{largura}} {len(g):>6}  {br(g[args.x].mean()):>{len(cab_x)}}  {br(g[args.y].mean()):>{len(cab_y)}}"
              f"  {pe:>7}  {sp:>8}")

    if args.influentes and col_id and len(tabela) > 3:
        total = tabela[[args.x, args.y]].corr().iloc[0, 1]
        mudancas = []
        for indice in tabela.index:
            resto = tabela.drop(index=indice)
            sem_ela = resto[[args.x, args.y]].corr().iloc[0, 1]
            mudancas.append((abs(sem_ela - total), indice, sem_ela))
        mudancas.sort(key=lambda m: (-m[0], m[1]))
        print()
        n = min(args.influentes, len(mudancas))
        quais = "a linha que mais mexe" if n == 1 else f"as {n} linhas que mais mexem"
        print(f"{quais} no Pearson de todas as linhas ({br(total, 2)}), tirando uma de cada vez")
        colunas = [col_id] + ([segmento] if segmento else []) + [args.x, args.y]
        print("  ".join(f"{c:>12}" for c in colunas) + f"  {'Pearson sem ela':>15}  {'mudança':>8}")
        for _, indice, sem_ela in mudancas[:args.influentes]:
            linha = tabela.loc[indice]
            valores = [str(linha[col_id])] + ([str(linha[segmento])] if segmento else [])
            valores += [br(linha[args.x], casas_de(tabela[args.x])), br(linha[args.y], casas_de(tabela[args.y]))]
            mudanca = ("+" if sem_ela - total >= 0 else "") + br(sem_ela - total, 2)
            print("  ".join(f"{v:>12}" for v in valores) + f"  {br(sem_ela, 2):>15}  {mudanca:>8}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
