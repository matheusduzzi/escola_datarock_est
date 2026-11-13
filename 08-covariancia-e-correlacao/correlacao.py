"""Covariância, Pearson e Spearman de cada coluna contra uma coluna-alvo, e a média do alvo por faixa.

Rode de dentro da pasta da aula:

    python3 correlacao.py                                  # dados/produtos.csv, alvo vendas
    python3 correlacao.py --multiplicar preco=100          # o preço em centavos, como o sistema exporta
    python3 correlacao.py --arquivo dados/entregas_abril.csv --alvo horas

O que cada conta faz, em pandas:
- covariância: tabela[col].cov(tabela[alvo]), dividida por n - 1. Tem a unidade das duas colunas
  multiplicadas (reais x unidades vendidas, por exemplo).
- Pearson: tabela[[col, alvo]].corr(method="pearson"). É a covariância dividida pelos dois desvios
  padrão: sai sem unidade, entre -1 e 1.
- Spearman: tabela[[col, alvo]].corr(method="spearman"). É o Pearson calculado nas posições
  (rank) de cada valor, e não nos valores. Empates ganham a posição média.
- faixas: a média do alvo em cada faixa da coluna. Coluna com até 13 valores diferentes usa cada
  valor; as outras são cortadas em 5 faixas com o mesmo número de linhas (pd.qcut).

Colunas que começam com "id" ficam de fora. Linhas com vazio na coluna ou no alvo saem só daquela conta.
"""
import argparse
import sys
from pathlib import Path

import pandas as pd

AQUI = Path(__file__).resolve().parent


def br(x, casas=1):
    texto = f"{x:,.{casas}f}"
    return texto.replace(",", "_").replace(".", ",").replace("_", ".")


def faixas(tabela, col, alvo):
    par = tabela[[col, alvo]].dropna()
    if par[col].nunique() <= 13:
        grupos = par.groupby(col)[alvo]
        rotulos = [br(v, 0) if float(v).is_integer() else br(v) for v in grupos.mean().index]
    else:
        cortes = pd.qcut(par[col], 5)
        grupos = par.groupby(cortes, observed=True)[alvo]
        casas = 0 if pd.api.types.is_integer_dtype(par[col]) else 1
        rotulos = []
        for intervalo in grupos.mean().index:
            dentro = par.loc[cortes == intervalo, col]
            rotulos.append(f"{br(dentro.min(), casas)} a {br(dentro.max(), casas)}")
    medias, contagens = grupos.mean(), grupos.count()
    linhas = [f"  {'faixa de ' + col:<24} {'linhas':>6}  média de {alvo}"]
    for rot, n, m in zip(rotulos, contagens, medias):
        linhas.append(f"  {rot:<24} {n:>6}  {br(m):>10}")
    return linhas


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--arquivo", default="dados/produtos.csv")
    p.add_argument("--alvo", default="vendas")
    p.add_argument("--multiplicar", action="append", default=[], metavar="COLUNA=FATOR",
                   help="troca a unidade de uma coluna antes das contas (pode repetir)")
    args = p.parse_args()

    caminho = Path(args.arquivo)
    if not caminho.is_absolute():
        caminho = AQUI / caminho
    if not caminho.is_file():
        sys.exit(f"Arquivo não encontrado: {args.arquivo}")
    tabela = pd.read_csv(caminho)
    if args.alvo not in tabela.columns:
        sys.exit(f"A coluna-alvo '{args.alvo}' não existe em {args.arquivo}. Colunas: {', '.join(tabela.columns)}")
    if len(tabela) < 3:
        sys.exit("São precisas pelo menos 3 linhas para calcular correlação.")

    trocas = []
    for item in args.multiplicar:
        col, _, fator = item.partition("=")
        if col not in tabela.columns:
            sys.exit(f"--multiplicar: a coluna '{col}' não existe em {args.arquivo}")
        try:
            fator = float(fator)
        except ValueError:
            sys.exit(f"--multiplicar: o fator de '{col}' precisa ser um número, por exemplo {col}=100")
        tabela[col] = tabela[col] * fator
        trocas.append(f"{col} x {br(fator, 0) if fator.is_integer() else br(fator, 3)}")

    colunas = [c for c in tabela.columns if c != args.alvo and not c.lower().startswith("id")
               and pd.api.types.is_numeric_dtype(tabela[c])]
    if not pd.api.types.is_numeric_dtype(tabela[args.alvo]) or not colunas:
        sys.exit("O alvo e pelo menos uma outra coluna precisam ser numéricos.")

    print(f"{caminho.name}: {len(tabela)} linhas | alvo: {args.alvo}")
    if trocas:
        print("unidade trocada: " + ", ".join(trocas))
    print()
    print(f"{'coluna':<14} {'covariância':>14} {'Pearson':>9} {'Spearman':>9}")
    for col in colunas:
        par = tabela[[col, args.alvo]]
        cov = par[col].cov(par[args.alvo])
        pearson = par.corr(method="pearson").iloc[0, 1]
        spearman = par.corr(method="spearman").iloc[0, 1]
        print(f"{col:<14} {br(cov):>14} {br(pearson, 2):>9} {br(spearman, 2):>9}")
    for col in colunas:
        print()
        print("\n".join(faixas(tabela, col, args.alvo)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
